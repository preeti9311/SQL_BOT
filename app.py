import streamlit as st
from pathlib import Path
import sqlite3
from langchain_classic.agents import AgentType
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_community.utilities import SQLDatabase
from langchain_community.callbacks.streamlit import StreamlitCallbackHandler
from langchain_community.agent_toolkits.sql.base import create_sql_agent
from sqlalchemy import create_engine
from langchain_groq import ChatGroq
from sqlalchemy.engine import URL


st.set_page_config(
    page_title=" DataPilot AI | Smart SQL Assistant",
    page_icon="🧠",
    layout="wide"
)
st.title("⚡DataPilot AI | Chat with Your Database")
st.write("Ask questions about your database and get answers in natural language.")

LOCALDB = "USE_LOCALDB"
MYSQL = "USE_MYSQL"

radio_opt = [
    "📂 SQLite — Local Database",
    "🌐 MySQL — Connect MYSQL Database"
]
radio = st.sidebar.radio(
    "Choose your database which you want to use:",
    options=radio_opt
)

if radio_opt.index(radio) == 1:
    db_uri = MYSQL
    mysql_host = st.sidebar.text_input("Provide Mysql Host")
    mysql_user = st.sidebar.text_input("Provide Mysql User")
    mysql_password = st.sidebar.text_input("Provide Mysql Password", type="password")
    mysql_database = st.sidebar.text_input("Provide Mysql Database")
else:
    db_uri = LOCALDB

api_key = st.sidebar.text_input(label="Provide Groq API Key", type="password")

if not db_uri:
    st.info("Please select a database type to continue.")

if not api_key:
    st.info("Please provide your Groq API Key to continue.")
    st.stop()

## LLM Model
llm = ChatGroq(
    groq_api_key=api_key,
    model="openai/gpt-oss-120b",
    temperature=0,
    streaming=True
)
@st.cache_resource(ttl="2h")
def configure_db(db_uri, mysql_host=None, mysql_user=None, mysql_password=None, mysql_database=None):
    if db_uri == LOCALDB:
        db_path = (Path(__file__).parent /"student.db").absolute()
        print(db_path)
        creator = lambda: sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
        return SQLDatabase(create_engine("sqlite://", creator=creator))

    elif db_uri == MYSQL:
        if not mysql_host or not mysql_user or not mysql_password or not mysql_database:
            st.error("Please provide all MySQL connection details.")
            st.stop()

        db_url = URL.create(
            drivername="mysql+mysqlconnector",
            username=mysql_user,
            password=mysql_password,
            host=mysql_host.strip(),
            port=3306,
            database=mysql_database
        )

        engine = create_engine(db_url)

        return SQLDatabase(engine)

if db_uri == MYSQL:
    db = configure_db(db_uri, mysql_host, mysql_user, mysql_password, mysql_database)
else:
    db = configure_db(db_uri)



# ✨ DataPilot AI — SQL Agent

st.markdown(
    """
    <div style="text-align:center; padding: 12px 0 20px 0;">
        <h1 style="margin-bottom:0;">🧠 DataPilot AI</h1>
        <p style="color:gray; font-size:16px;">
            ✦ Your data, your questions, instant insights ✦
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# SQL Toolkit
toolkit = SQLDatabaseToolkit(db=db, llm=llm)

agent = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    agent_type="tool-calling",
    verbose=True,
    handle_parsing_errors=True,
    prefix="""
    You are DataPilot AI, an expert SQL data analyst.

    Your job is to answer database questions accurately and in detail.

    Instructions:
    1. Always inspect the database schema before writing SQL queries when needed.
    2. Use SQL queries to retrieve actual database information.
    3. Never make up or assume database values.
    4. Explain the query results in simple and understandable language.
    5. For multiple records, present results in a clear table whenever appropriate.
    6. For aggregate queries, explain the calculations and their meaning.
    7. When the user asks for analysis, provide detailed insights.
    8. Include important observations and patterns in the data.
    9. If the result contains many records, summarize the key findings.
    10. If a question is unclear, ask for clarification.
    11. Keep answers organized using headings and bullet points.
    12. Always provide a meaningful conclusion.

    Give detailed answers while staying relevant to the user's question.
    """
)
# Chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {
            "role": "assistant",
            "content": "👋 Hey! I'm DataPilot AI. Ask me anything about your database."
        }
    ]

if st.sidebar.button("🗑️ Clear Chat", use_container_width=True):
    st.session_state["messages"] = [
        {
            "role": "assistant",
            "content": "👋 Hey! I'm DataPilot AI. Ask me anything about your database."
        }
    ]
    st.rerun()

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(
        msg["role"],
        avatar="🧠" if msg["role"] == "assistant" else "🧑‍💻"
    ):
        st.markdown(msg["content"])

# User input
user_query = st.chat_input(
    "💬 Ask a question about your database..."
)

if user_query:
    st.session_state.messages.append(
        {"role": "user", "content": user_query}
    )

    with st.chat_message("user", avatar="🧑‍💻"):
        st.markdown(user_query)

    with st.chat_message("assistant", avatar="🧠"):
        streamlit_callback = StreamlitCallbackHandler(
            st.container(),
            expand_new_thoughts=True
        )

        try:
            result = agent.invoke(
                {"input": user_query},
                config={"callbacks": [streamlit_callback]}
            )
            response = result["output"]
            st.markdown(response)

        except Exception:
            response = (
                "⚠️ Something went wrong while processing your query. "
                "Please check your API key, database connection, and logs."
            )
            st.error(response)

        st.session_state.messages.append(
            {"role": "assistant", "content": response}
        )

