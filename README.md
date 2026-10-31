# 🧠 DataPilot AI – Smart SQL Assistant

An AI-powered SQL chatbot that lets you interact with databases using natural language instead of writing SQL queries manually.

## 🚀 Features

- 🤖 AI-powered SQL assistant
- 💬 Natural language to SQL queries
- 🗄️ SQLite and MySQL database support
- ⚡ Powered by Groq LLM (`openai/gpt-oss-120b`)
- 🔍 Automatic SQL query generation and execution
- 📊 Detailed database insights and explanations
- 💬 Interactive chat history
- 🎨 Streamlit-based user interface

## 🛠️ Tech Stack

- Python
- Streamlit
- LangChain
- LangChain Community
- Groq API
- SQLAlchemy
- SQLite
- MySQL

## 📁 Project Structure

```text
SQL_BOT/
├── app.py
├── student.db
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/preeti9311/SQL_BOT.git
```

### 2. Navigate to the project

```bash
cd SQL_BOT
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

Activate on Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Get your Groq API key

Get your API key from:

https://console.groq.com/keys

### 6. Run the application

```bash
streamlit run app.py
```

## 🗄️ Database Configuration

**SQLite**
- Select SQLite in the sidebar.
- Connect to the local `student.db` database.

**MySQL**
- Select MySQL in the sidebar.
- Enter your host, username, password, and database name.

## ☁️ Deployment on Render

Build Command:

```bash
pip install -r requirements.txt
```

Start Command:

```bash
streamlit run app.py --server.port $PORT --server.address 0.0.0.0
```

Configure your Groq API key securely in the Render environment variables or Streamlit secrets.

## 🔐 Security

- Never commit API keys or database passwords.
- Keep sensitive database files out of public repositories.
- Use secure database credentials.

## 🎯 Project Objective

DataPilot AI aims to simplify database management and data analysis by allowing users to ask questions in natural language and receive meaningful insights from their databases.

## 👩‍💻 Author

**Preeti**

GitHub: [preeti9311](https://github.com/preeti9311)

Project Repository: [SQL_BOT](https://github.com/preeti9311/SQL_BOT)

---
