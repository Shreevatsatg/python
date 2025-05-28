import mysql.connector
conn=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    buffered=True,)
cursor = conn.cursor()

def insert_rows(empno,name,salary):
    st="select * from employee where empno='%d'"
    arg=(empno,)
    cursor.execute(st % arg)
    if cursor.rowcount >= 1:
        print("Record already exists")
    else:
        st="insert into employee(empno,name,salary) values(%d,'%s',%d)"
        arg=(empno,name,salary)
        cursor.execute(st % arg)
        conn.commit()
        print("Record inserted successfully")

def display_specific(empno):
    st="select * from employee where empno='%d'"
    cursor.execute(st % empno)
    if cursor.rowcount > 0:
        row = cursor.fetchone()
        print(row)
    else:
        print("No record found with that employee number")

def display_range(low, high):
    st="select * from employee where salary between %d and %d"
    arg=(low, high)
    cursor.execute(st % arg)
    if cursor.rowcount > 0:
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    else:
        print("No records found in that salary range")

if __name__ == "__main__":
    while True:
        print("1. Insert Record")
        print("2. Display Specific Record")
        print("3. Display Records in Salary Range")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            n= int(input("Enter number of employees to insert: "))
            for i in range(n):
                empno = int(input("Enter employee number: "))
                name = input("Enter employee name: ")
                salary = int(input("Enter employee salary: "))
                insert_rows(empno, name, salary)
        elif choice == 2:
            empno = int(input("Enter employee number to display: "))
            display_specific(empno)
        elif choice == 3:
            low = int(input("Enter lower salary limit: "))
            high = int(input("Enter upper salary limit: "))
            display_range(low, high)
        elif choice == 4:
            break
        else:
            print("Invalid choice, please try again.")
cursor.close()
conn.close()