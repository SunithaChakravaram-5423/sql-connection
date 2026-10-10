import pyodbc
connection_string = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=ACU-HYD-LT-2017\\SQLEXPRESS;"
    "DATABASE=StudentDB;"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)

connection = pyodbc.connect(connection_string)
cursor = connection.cursor()
print("Connected")


cursor.execute("SELECT * from Students")

for row in cursor.fetchall():
    print(row[0], row[1], format(row[2], '.2f'), format(row[3], '.2f'), format(row[4], '.2f'))


def add_student():
    Name = input("Enter name : ")
    English = float(input("Enetr English marks: "))
    Maths = float(input("Enter Maths marks: "))
    Science = float(input("Enter Science marks"))
    
    if not Name:
        print("Fields cannot be empty")
        return
    if not all(0 <= mark <= 100 for mark in [English, Maths, Science]):
        print("Invalid marks")
        return
    query ="""
    INSERT into Students(Name, English, Maths, Science) values(?,?,?,?)
    """
    cursor.execute(query, (Name, English, Maths, Science))
    connection.commit()
    
    print("Student added successfully")

    

def view_student():
    cursor.execute("SELECT * FROM Students")
    for row in cursor.fetchall():
        print(row[0], row[1],format(row[2], '.2f'),format(row[3], '.2f'),format(row[4], '.2f')
    )   
        


def update_student(Id):
    new_Maths =float(input("ENter new maths marks: "))
    if not 0<=new_Maths<=100:
        print("Invalid Marks")
        return
    query="""
    update Students set Maths = ? where Id = ?
    """
    cursor.execute(query, (new_Maths, Id))
    connection.commit()
    if cursor.rowcount > 0:
        print("Student updated successfully!")
    else:
        print("Student not found!")
        
        
def delete_student():
    new_Id = int(input("Enter Id to be deleted"))
    query = """
    delete from Students where Id = ?
    """
    cursor.execute(query, (new_Id,))
    connection.commit()
    if cursor.rowcount > 0:
        print("Student deleted successfully!")
    else:
        print("Student not found!")



def studenst_above_avg():
    avg = float(input("ENter min avg"))
    query="""
    select Id, Name, English, Maths, Science, (English+Maths+Science)/3.0 as Average
    from Students
    where (English+Maths+Science)/3.0 > ?
    order by Average desc
    """
    
    cursor.execute(query, (avg,))
    connection.commit()
    
    for row in cursor.fetchall():
        print(row[0], row[1], format(row[5], '.2f'))

while True:
    print("-------Student Grade Tracker-------")
    print("1.Add Student")
    print("2.View Students")
    print("3.Update Students")
    print("4.Delete Student")
    print("5. Students Above Average")
    print("6.Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        add_student()
    elif choice == 2:
        view_student()
    elif choice == 3:
        student_id = int(input("Enter student ID: "))
        update_student(student_id)
    elif choice == 4:
        delete_student()
    elif choice == 5:
        studenst_above_avg()
    elif choice == 6:
        print("Exiting Student Grade Tracker...")
        break
    else:
        print("Invalid choice")

cursor.close()
connection.close()