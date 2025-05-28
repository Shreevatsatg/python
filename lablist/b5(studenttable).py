import mysql.connector
conn=mysql.connector.connect(
    host='localhost',
    database='test',
    user='root',
    password='',
    buffered=True)
cursor =conn.cursor()

def insert_rows(rno,sname,s1,s2,s3):
    st="select * from student where rollno='%d' and name='%s'"
    arg=(rno,sname)
    cursor.execute(st % arg)
    if cursor.rowcount>=1:
        print("Record already exists")
    else:
        st="insert into student(rollno,name,s1,s2,s3) values(%d,'%s',%d,%d,%d)"
        arg=(rno,sname,s1,s2,s3)
        cursor.execute(st % arg)
        conn.commit()
        print("Record inserted successfully")

def display_all():
    st="select * from student"
    cursor.execute(st)
    if  cursor.rowcount>0:
        rows=cursor.fetchall()
        for row in rows:
            print(row)
    else:
        print("No records found")

def delete_specific(rno):
    st="delete from student where rollno='%d'"
    cursor.execute(st % rno)
    if cursor.rowcount>0:
        print("Record deleted successfully")
    else:
        print("No record found with that roll number")


if __name__ == "__main__":
    while True:
        print("1. Insert Record")
        print("2. Display All Records")
        print("3. Delete Specific Record")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            n= int(input("enter  number of students to insert: "))
            for i in range(n):
                rno = int(input("Enter roll number: "))
                sname = input("Enter student name: ")
                s1 = int(input("Enter score 1: "))
                s2 = int(input("Enter score 2: "))
                s3 = int(input("Enter score 3: "))
                insert_rows(rno, sname, s1, s2, s3)
        elif choice == 2:
            display_all()
        elif choice == 3:
            rno = int(input("Enter roll number to delete: "))
            delete_specific(rno)
        elif choice == 4:
            break
        else:
            print("Invalid choice, please try again.")
cursor.close()
conn.close()