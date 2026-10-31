
import sqlite3
conn = sqlite3.connect("student.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Student (
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS INT
)
""")

# Student data with technology courses
student_data = [
    ("Aarav", "Data Science", "A", 95),
    ("Priya", "DevOps", "B", 88),
    ("Rahul", "Artificial Intelligence", "A", 76),
    ("Sneha", "Machine Learning", "C", 92),
    ("Arjun", "Web Development", "A", 81),
    ("Ananya", "Cyber Security", "B", 97),
    ("Vikram", "Cloud Computing", "A", 65),
    ("Isha", "Data Science", "C", 89),
    ("Rohan", "DevOps", "A", 73),
    ("Meera", "Machine Learning", "B", 91),
    ("Karan", "Artificial Intelligence", "A", 84),
    ("Neha", "Web Development", "C", 78),
    ("Aditya", "Cyber Security", "A", 96),
    ("Kavya", "Cloud Computing", "B", 87),
    ("Sahil", "Data Science", "A", 69),
    ("Diya", "DevOps", "C", 93),
    ("Aman", "Machine Learning", "B", 55),
    ("Pooja", "Artificial Intelligence", "A", 74),
    ("Yash", "Web Development", "C", 82),
    ("Riya", "Cyber Security", "B", 99),
    ("Kabir", "Cloud Computing", "A", 67),
    ("Tanya", "Data Analytics", "C", 85),
    ("Dev", "Data Science", "B", 90),
    ("Simran", "DevOps", "A", 72),
    ("Manav", "Blockchain", "C", 83),
    ("Aditi", "Machine Learning", "A", 94),
    ("Nikhil", "Cyber Security", "B", 61),
    ("Shreya", "Cloud Computing", "C", 86),
    ("Varun", "Data Analytics", "A", 79),
    ("Muskan", "Artificial Intelligence", "B", 98),
    ("Harsh", "DevOps", "C", 77),
    ("Pallavi", "Web Development", "A", 89),
    ("Rajat", "Data Science", "B", 91),
    ("Nisha", "Blockchain", "C", 68),
    ("Siddharth", "Machine Learning", "A", 95),
    ("Tanvi", "Cloud Computing", "B", 81),
    ("Akash", "Data Analytics", "C", 74),
    ("Komal", "Cyber Security", "A", 88),
    ("Mohit", "DevOps", "B", 93),
    ("Ritika", "Artificial Intelligence", "C", 64),
    ("Saurabh", "Web Development", "A", 87),
    ("Divya", "Data Science", "B", 76),
    ("Abhishek", "Cloud Computing", "C", 85),
    ("Payal", "Machine Learning", "A", 97),
    ("Gaurav", "DevOps", "B", 62),
    ("Sakshi", "Cyber Security", "C", 91),
    ("Varsha", "Data Analytics", "A", 72),
    ("Deepak", "Artificial Intelligence", "B", 84),
    ("Naman", "Data Science", "C", 96),
    ("Khushi", "Blockchain", "A", 79),
    ("Pranav", "DevOps", "B", 88),
    ("Ishita", "Machine Learning", "C", 75),
    ("Tarun", "Cyber Security", "A", 93),
    ("Manya", "Web Development", "B", 82),
    ("Kunal", "Cloud Computing", "C", 66),
    ("Jhanvi", "Data Analytics", "A", 90),
    ("Rishi", "Data Science", "B", 86),
    ("Alisha", "Artificial Intelligence", "C", 95),
    ("Om", "DevOps", "A", 80),
    ("Navya", "Blockchain", "B", 77),
    ("Aryan", "Machine Learning", "C", 89),
    ("Bhavna", "Cyber Security", "A", 63),
    ("Parth", "Cloud Computing", "B", 98),
    ("Myra", "Data Analytics", "C", 92),
    ("Ankit", "Web Development", "A", 71),
    ("Juhi", "Data Science", "B", 87),
    ("Lakshya", "DevOps", "C", 94),
    ("Radhika", "Artificial Intelligence", "A", 68),
    ("Chirag", "Machine Learning", "B", 80),
    ("Priti", "Cyber Security", "C", 99),
    ("Sameer", "Cloud Computing", "A", 76),
    ("Sanya", "Data Analytics", "B", 85),
    ("Danish", "Blockchain", "C", 92),
    ("Nandini", "Web Development", "A", 73),
    ("Yuvraj", "DevOps", "B", 87),
    ("Saloni", "Data Science", "C", 96),
    ("Abhay", "Artificial Intelligence", "A", 64),
    ("Trisha", "Machine Learning", "B", 90),
    ("Raghav", "Cyber Security", "C", 82),
    ("Palak", "Cloud Computing", "A", 79),
    ("Keshav", "Data Analytics", "B", 97),
    ("Ayesha", "Blockchain", "C", 84),
    ("Ritesh", "DevOps", "A", 69),
    ("Mahima", "Data Science", "B", 91),
    ("Pratik", "Web Development", "C", 75),
    ("Suhani", "Artificial Intelligence", "A", 86),
    ("Ashwin", "Machine Learning", "B", 93),
    ("Garima", "Cyber Security", "C", 70),
    ("Ansh", "Cloud Computing", "A", 98),
    ("Reema", "Data Analytics", "B", 61),
    ("Nakul", "DevOps", "C", 89),
    ("Vanshika", "Blockchain", "A", 83),
    ("Dhruv", "Data Science", "B", 72),
    ("Kritika", "Cyber Security", "C", 94),
    ("Shivam", "Web Development", "A", 78),
    ("Aanchal", "Artificial Intelligence", "B", 88),
    ("Veer", "Machine Learning", "C", 65),
    ("Tara", "Cloud Computing", "A", 92),
    ("Prisha", "Data Analytics", "B", 81),
    ("Reyansh", "DevOps", "C", 100)
]


# Insert records
cursor.executemany("""
INSERT INTO Student (NAME, CLASS, SECTION, MARKS)
VALUES (?, ?, ?, ?)
""", student_data)

conn.commit()

# Verify data
cursor.execute("SELECT COUNT(*) FROM Student")
print("Total students:", cursor.fetchone()[0])

cursor.execute("SELECT DISTINCT CLASS FROM Student")
print("Available courses:")
for row in cursor.fetchall():
    print(row[0])

cursor.execute("SELECT * FROM Student")
print("All students:")
for row in cursor.fetchall():
    print(row)


# Additional student data
more_student_data = [
    ("Ishaan", "Data Science", "A", 88),
    ("Kiara", "DevOps", "B", 76),
    ("Rudra", "Artificial Intelligence", "C", 91),
    ("Avni", "Machine Learning", "A", 84),
    ("Rehan", "Cyber Security", "B", 72),
    ("Siya", "Cloud Computing", "C", 96),
    ("Atharv", "Web Development", "A", 67),
    ("Pari", "Data Analytics", "B", 89),
    ("Vivaan", "Blockchain", "C", 93),
    ("Anika", "Data Science", "B", 79),
    ("Krish", "DevOps", "A", 95),
    ("Aarohi", "Artificial Intelligence", "B", 86),
    ("Samarth", "Machine Learning", "C", 74),
    ("Mishka", "Cyber Security", "A", 90),
    ("Zoya", "Cloud Computing", "B", 81),
    ("Ritvik", "Web Development", "C", 77),
    ("Amaira", "Data Analytics", "A", 98),
    ("Neil", "Blockchain", "B", 69),
    ("Ayesha", "Data Science", "C", 92),
    ("Darsh", "DevOps", "B", 83),
    ("Aarush", "Artificial Intelligence", "A", 87),
    ("Saanvi", "Machine Learning", "B", 94),
    ("Kabir", "Cyber Security", "C", 65),
    ("Mysha", "Cloud Computing", "A", 88),
    ("Yug", "Web Development", "B", 73),
    ("Inaya", "Data Analytics", "C", 91),
    ("Shaurya", "Blockchain", "A", 80),
    ("Prisha", "Data Science", "B", 97),
    ("Devansh", "DevOps", "C", 62),
    ("Navya", "Artificial Intelligence", "A", 85),
    ("Abeer", "Machine Learning", "B", 78),
    ("Ira", "Cyber Security", "C", 96),
    ("Kiaan", "Cloud Computing", "A", 71),
    ("Vanya", "Web Development", "B", 89),
    ("Arnav", "Data Analytics", "C", 82),
    ("Mahira", "Blockchain", "A", 93),
    ("Reyanshi", "Data Science", "B", 68),
    ("Laksh", "DevOps", "C", 90),
    ("Aadhya", "Artificial Intelligence", "A", 99),
    ("Vihaan", "Machine Learning", "B", 75),
    ("Saira", "Cyber Security", "C", 84),
    ("Dhruv", "Cloud Computing", "A", 92),
    ("Aarika", "Web Development", "B", 66),
    ("Parth", "Data Analytics", "C", 87),
    ("Ronav", "Blockchain", "A", 76),
    ("Jiya", "Data Science", "B", 95),
    ("Advait", "DevOps", "C", 81),
    ("Aahana", "Artificial Intelligence", "A", 73),
    ("Yashvi", "Machine Learning", "B", 89),
    ("Riaan", "Cyber Security", "C", 98)
]

# Combine both lists
student_data.extend(more_student_data)

# Insert all records
cursor.executemany("""
INSERT INTO Student (NAME, CLASS, SECTION, MARKS)
VALUES (?, ?, ?, ?)
""", student_data)

conn.commit()

# Verify records
cursor.execute("SELECT COUNT(*) FROM Student")
print("Total students:", cursor.fetchone()[0])

# Show all available courses
cursor.execute("SELECT DISTINCT CLASS FROM Student")
print("Available courses:")
for row in cursor.fetchall():
    print(row[0])

conn.close()
