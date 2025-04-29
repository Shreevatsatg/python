class employee:
    def getemployee(self):
        self.empno=int(input('Employee number: '))
        self.empname=input('Employee Name: ')
        self.dept=input('Department: ')
        self.design=input('Designation: ')
        self.age=int(input('Age: '))
        self.salary=int(input('Salary: '))

    def display(self):
        print(self.empno,"\t",self.empname,"\t",self.dept,"\t",self.design,"\t",self.age,"\t",self.salary)

    def search(self,id):
        if(self.empno==id):
            return True
        else:
            return False

while True:
    print('\n\t\tEMPLOYEE INFORMATION')
    print('1.CREATE EMPLOYEE INFORMATION')
    print('2.DISPLAY EMPLOYEE INFORMATION')
    print('3.SEARCH FOR AN EMPLOYEE')
    print('4.EXIT')
    ch=int(input('Enter your choice: '))
    if ch==1:
        print('-'*30)
        n=int(input('Enter number of employees: '))
        l=[]
        for i in range(n):
            e=employee()
            e.getemployee()
            l.append(e)
    elif ch==2:
        print("EMPNO\tEMPNAME\tDEPARTMENT\tDESIGNATION\tAGE\tSALARY")
        for i in l:
            i.display()
    elif ch==3:
        print('*'*30)
        id=int(input('Enter Employee Number'))
        for i in l:
            found=i.search(id)
            if(found):
                print("EMPNO\tEMPNAME\t\tDEPARTMENT\tDESIGNATION\tAGE\tSALARY")
                i.display()
                break
        if not found:
            print('This Employee ID does not exist!!!!')
    elif ch==4:
        break
    else:
        print('Invalid Choice')


