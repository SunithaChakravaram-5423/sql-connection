# # import psycopg
# # conn = psycopg.connect("postgresql://neondb_owner:npg_J1NCr0fZbxwi@ep-shy-wildflower-aevc47o4-pooler.c-2.us-east-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require")
# # cur = conn.cursor()
# # cur.execute("Drop table if exists students")
# # cur.execute("SELECT version();")
# # # Create table
# # cur.execute("""
# #     CREATE TABLE IF NOT EXISTS students (
# #         id INTEGER PRIMARY KEY,
# #         name TEXT,
# #         age INTEGER
# #     )
# # """)

# # # Insert data
# # cur.execute(
# #     "INSERT INTO students (id, name, age) VALUES (%s, %s, %s)",
# #     (1, "Rahul", 20)
# # )

# # # cur.execute(
# # #     "INSERT INTO students (id, name, age) VALUES (%s, %s, %s)",
# # #     (2, "Priya", 21)
# # # )

# # # conn.commit()

# # # # Read data
# # # cur.execute("SELECT name FROM students")

# # # for row in cur.fetchall():
# # #     print(row[0])

# # # conn.close()

# # import psycopg
# # connection_string = "postgresql://neondb_owner:npg_J1NCr0fZbxwi@ep-shy-wildflower-aevc47o4-pooler.c-2.us-east-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require"
# # conn = psycopg.connect(connection_string)
# # cursor = conn.cursor()
# # cursor.execute("SELECT version();")
# # result = cursor.fetchone()
# # print(result)
# # cursor. close()
# # conn.close()

# # import psycopg
# # connection_string = "postgresql://neondb_owner:npg_J1NCr0fZbxwi@ep-shy-wildflower-aevc47o4-pooler.c-2.us-east-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require"
# # conn = psycopg.connect(connection_string)
# # cursor = conn.cursor()
# # id = int(input("Enter student id:"))
# # name=input("Enter Name:")
# # age=int(input("Enter age :"))
# # create_table_query = """CREATE TABLE IF NOT EXISTS students (
# #         id SERIAL PRIMARY KEY,
# #         name VARCHAR(100),
# #         age INT,
# #         marks INT
# #     )"""
# # insert_query = """
# #     INSERT INTO students (id, name, age)
# #     VALUES (%s, %s, %s)
# # """
# # get_data_query = "SELECT * FROM students"
# # cursor.execute(create_table_query)
# # cursor.execute(insert_query, (id, name, age))
# # cursor.execute(get_data_query)
# # students = cursor.fetchall()
# # for student in students:
# #     print(student)
# # conn.commit()
# # print("Table created successfully!")
# # cursor.close()
# # conn.close()
 
# import psycopg
# connection_string = "postgresql://neondb_owner:npg_J1NCr0fZbxwi@ep-shy-wildflower-aevc47o4-pooler.c-2.us-east-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require"
# conn = psycopg.connect(connection_string)
# cursor = conn.cursor()
# create_table_query = """CREATE TABLE IF NOT EXISTS students (
#         id SERIAL PRIMARY KEY,
#         name VARCHAR(100),
#         age INT
#     )"""
# insert_query = """
# INSERT INTO students (id, name, age) VALUES (1, 'Rahul', 20);
# INSERT INTO students (id, name, age) VALUES (2, 'Priya', 21);
# INSERT INTO students (id, name, age) VALUES (3, 'Arjun', 19);
# INSERT INTO students (id, name, age) VALUES (4, 'Sneha', 22);
# INSERT INTO students (id, name, age) VALUES (5, 'Kiran', 20);
# INSERT INTO students (id, name, age) VALUES (6, 'Ananya', 21);
# INSERT INTO students (id, name, age) VALUES (7, 'Vikram', 23);
# INSERT INTO students (id, name, age) VALUES (8, 'Pooja', 20);
# INSERT INTO students (id, name, age) VALUES (9, 'Rohan', 22);
# INSERT INTO students (id, name, age) VALUES (10, 'Divya', 21);
# INSERT INTO students (id, name, age) VALUES (11, 'Aman', 19);
# INSERT INTO students (id, name, age) VALUES (12, 'Neha', 20);
# INSERT INTO students (id, name, age) VALUES (13, 'Suresh', 23);
# INSERT INTO students (id, name, age) VALUES (14, 'Kavya', 21);
# INSERT INTO students (id, name, age) VALUES (15, 'Ravi', 22);
# INSERT INTO students (id, name, age) VALUES (16, 'Meena', 20);
# INSERT INTO students (id, name, age) VALUES (17, 'Nikhil', 19);
# INSERT INTO students (id, name, age) VALUES (18, 'Swathi', 21);
# INSERT INTO students (id, name, age) VALUES (19, 'Karthik', 22);
# INSERT INTO students (id, name, age) VALUES (20, 'Harini', 20);
# INSERT INTO students (id, name, age) VALUES (21, 'Manoj', 23);
# INSERT INTO students (id, name, age) VALUES (22, 'Lakshmi', 21);
# INSERT INTO students (id, name, age) VALUES (23, 'Ajay', 20);
# INSERT INTO students (id, name, age) VALUES (24, 'Keerthi', 22);
# INSERT INTO students (id, name, age) VALUES (25, 'Varun', 19);
# INSERT INTO students (id, name, age) VALUES (26, 'Shreya', 21);
# INSERT INTO students (id, name, age) VALUES (27, 'Rakesh', 23);
# INSERT INTO students (id, name, age) VALUES (28, 'Aishwarya', 20);
# INSERT INTO students (id, name, age) VALUES (29, 'Tarun', 22);
# INSERT INTO students (id, name, age) VALUES (30, 'Nandini', 21);
# INSERT INTO students (id, name, age) VALUES (31, 'Sanjay', 20);
# INSERT INTO students (id, name, age) VALUES (32, 'Deepika', 19);
# INSERT INTO students (id, name, age) VALUES (33, 'Prakash', 23);
# INSERT INTO students (id, name, age) VALUES (34, 'Ishita', 21);
# INSERT INTO students (id, name, age) VALUES (35, 'Rohit', 22);
# INSERT INTO students (id, name, age) VALUES (36, 'Bhavya', 20);
# INSERT INTO students (id, name, age) VALUES (37, 'Abhishek', 19);
# INSERT INTO students (id, name, age) VALUES (38, 'Madhuri', 21);
# INSERT INTO students (id, name, age) VALUES (39, 'Siddharth', 22);
# INSERT INTO students (id, name, age) VALUES (40, 'Tejaswini', 20);
# INSERT INTO students (id, name, age) VALUES (41, 'Aditya', 23);
# INSERT INTO students (id, name, age) VALUES (42, 'Pallavi', 21);
# INSERT INTO students (id, name, age) VALUES (43, 'Gaurav', 20);
# INSERT INTO students (id, name, age) VALUES (44, 'Sowmya', 22);
# INSERT INTO students (id, name, age) VALUES (45, 'Varsha', 19);
# INSERT INTO students (id, name, age) VALUES (46, 'Rahul', 21);
# INSERT INTO students (id, name, age) VALUES (47, 'Preethi', 20);
# INSERT INTO students (id, name, age) VALUES (48, 'Naveen', 23);
# INSERT INTO students (id, name, age) VALUES (49, 'Akshara', 21);
# INSERT INTO students (id, name, age) VALUES (50, 'Chaitanya', 22);
# INSERT INTO students (id, name, age) VALUES (51, 'Bhargavi', 20);
# INSERT INTO students (id, name, age) VALUES (52, 'Vamshi', 19);
# INSERT INTO students (id, name, age) VALUES (53, 'Reshma', 21);
# INSERT INTO students (id, name, age) VALUES (54, 'Abhinav', 22);
# INSERT INTO students (id, name, age) VALUES (55, 'Teja', 20);
# INSERT INTO students (id, name, age) VALUES (56, 'Mounika', 23);
# INSERT INTO students (id, name, age) VALUES (57, 'Varun', 21);
# INSERT INTO students (id, name, age) VALUES (58, 'Sahithi', 20);
# INSERT INTO students (id, name, age) VALUES (59, 'Harsha', 19);
# INSERT INTO students (id, name, age) VALUES (60, 'Sravani', 22);
# INSERT INTO students (id, name, age) VALUES (61, 'Mahesh', 21);
# INSERT INTO students (id, name, age) VALUES (62, 'Lavanya', 20);
# INSERT INTO students (id, name, age) VALUES (63, 'Sai', 23);
# INSERT INTO students (id, name, age) VALUES (64, 'Sindhu', 21);
# INSERT INTO students (id, name, age) VALUES (65, 'Raghu', 22);
# INSERT INTO students (id, name, age) VALUES (66, 'Nitya', 20);
# INSERT INTO students (id, name, age) VALUES (67, 'Surya', 19);
# INSERT INTO students (id, name, age) VALUES (68, 'Hema', 21);
# INSERT INTO students (id, name, age) VALUES (69, 'Pranav', 22);
# INSERT INTO students (id, name, age) VALUES (70, 'Mouni', 20);
# INSERT INTO students (id, name, age) VALUES (71, 'Yash', 23);
# INSERT INTO students (id, name, age) VALUES (72, 'Riya', 21);
# INSERT INTO students (id, name, age) VALUES (73, 'Abhay', 20);
# INSERT INTO students (id, name, age) VALUES (74, 'Pavani', 19);
# INSERT INTO students (id, name, age) VALUES (75, 'Kunal', 22);
# INSERT INTO students (id, name, age) VALUES (76, 'Rachana', 21);
# INSERT INTO students (id, name, age) VALUES (77, 'Vishal', 20);
# INSERT INTO students (id, name, age) VALUES (78, 'Apoorva', 23);
# INSERT INTO students (id, name, age) VALUES (79, 'Sandeep', 21);
# INSERT INTO students (id, name, age) VALUES (80, 'Sushma', 20);
# INSERT INTO students (id, name, age) VALUES (81, 'Rahul', 19);
# INSERT INTO students (id, name, age) VALUES (82, 'Pooja', 22);
# INSERT INTO students (id, name, age) VALUES (83, 'Kiran', 21);
# INSERT INTO students (id, name, age) VALUES (84, 'Anjali', 20);
# INSERT INTO students (id, name, age) VALUES (85, 'Ramesh', 23);
# INSERT INTO students (id, name, age) VALUES (86, 'Shalini', 21);
# INSERT INTO students (id, name, age) VALUES (87, 'Naveen', 20);
# INSERT INTO students (id, name, age) VALUES (88, 'Divya', 19);
# INSERT INTO students (id, name, age) VALUES (89, 'Karthik', 22);
# INSERT INTO students (id, name, age) VALUES (90, 'Manasa', 21);
# INSERT INTO students (id, name, age) VALUES (91, 'Suresh', 20);
# INSERT INTO students (id, name, age) VALUES (92, 'Kavya', 23);
# INSERT INTO students (id, name, age) VALUES (93, 'Arun', 21);
# INSERT INTO students (id, name, age) VALUES (94, 'Sneha', 20);
# INSERT INTO students (id, name, age) VALUES (95, 'Ravi', 19);
# INSERT INTO students (id, name, age) VALUES (96, 'Meena', 22);
# INSERT INTO students (id, name, age) VALUES (97, 'Nikhil', 21);
# INSERT INTO students (id, name, age) VALUES (98, 'Swathi', 20);
# INSERT INTO students (id, name, age) VALUES (99, 'Vikram', 23);
# INSERT INTO students (id, name, age) VALUES (100, 'Harini', 21);
# """
# cursor.execute("DROP TABLE IF EXISTS students")
# get_data_query = "SELECT * FROM students"
# cursor.execute(create_table_query)
# cursor.execute(insert_query)
# cursor.execute(get_data_query)
# cursor.execute("select * from students order by age")
# students = cursor.fetchall()
# for student in students:
#     print(student)
# conn.commit()
# print("Students data created successfully!")
# cursor.close()
# conn.close()


import psycopg
import random
conn = psycopg.connect("postgresql://neondb_owner:npg_J1NCr0fZbxwi@ep-shy-wildflower-aevc47o4-pooler.c-2.us-east-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require")
cur = conn.cursor()
# Create table

def create_tabel():
    cur.execute("DROP TABLE IF EXISTS students")
    cur.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
    """)
    print("Table Created")

def insert_values():
    for i in range(1, 21):
        cur.execute(
            "INSERT INTO students VALUES (%s, %s, %s)",
            (i, f"Student{i}", random.randint(18, 30))
        )
    cur.execute("SELECT * from students")
    students = cur.fetchall()
    for student in students:
        print(student)
    print("Students inserted successfully")
def delete_values():
    cur.execute("DELETE FROM students")
    print("DELETED from table")

    cur.execute("SELECT * FROM students")
    students = cur.fetchall()

    if len(students) == 0:
        print("Table is empty")
    else:
        for student in students:
            print(student)    
def exit_table():
    print("EXIT")
while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Create Students Table")
    print("2. Insert Student")
    print("3. Delete Student")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice==1:
        create_tabel()
        conn.commit()
    elif choice==2:
        insert_values()
        conn.commit()
    elif choice==3:
        delete_values()
        conn.commit()
    elif choice == 4:
        exit_table()
        break
    else:
        print("Enter the appropriate choice : 1,2,3 or 4")

cur.close()
conn.close()