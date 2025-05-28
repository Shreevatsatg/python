import mysql.connector
conn=mysql.connector.connect(host='localhost',database='detailes',user='root',password='',buffered=True)
cursor=conn.cursor()

def insert_rows(tc,cn,mno,pr,cr):
    st="select * from electricitybill where mno='%d'"
    arg=(mno)
    cursor.execute(st % arg)
    if cursor.rowcount>=1:
        print("Meter no exists")
    else:
        st="insert into electricitybill values('%s','%s','%d','%d','%d')"
        arg=(tc,cn,mno,pr,cr)
        cursor.execute(st % arg)
        conn.commit()
        print('Record inserted..')

def update_reading(mno):
    st="select * from electricitybill where mno='%d'"
    arg=(mno)
    cursor.execute(st % arg)
    if cursor.rowcount>0:
        row=cursor.fetchone()
        print(row)
        cr=int(input("Enter current meter reading: "))
        pr=row[4]
        if cr>pr:
            st="update electricitybill set pr='%d', cr='%d' where mno='%d'"
            arg=(pr,cr,mno)
            cursor.execute(st % arg)
            print('\nReading Updated')
        else:
            print('Current meter reading must be greater than previous reading')
    else:
        print('Meter no does not exist')

def calculate_bill(mno):
    st="select * from electricitybill where mno='%d'"
    arg=(mno)
    cursor.execute(st % arg)
    if cursor.rowcount>0:
        row=cursor.fetchone()
        units=row[4]-row[3]
        if row[0]=='LT1':
            if units<=30:
                bill=units*2
            elif units<=100:
                bill=30*2+(units-30)*3.5
            elif units<=200:
                bill=30*2+70*3.5+(units-100)*4.5
            else:
                bill=30*2+70*3.5+100*4.5+(units-200)*5
        else:
            if units<=30:
                bill=units*3.5
            elif units<=100:
                bill=30*3.5+(units-30)*5
            elif units<=200:
                bill=30*3.5+70*5+(units-100)*6
            else:
                bill=30*3.5+70*5+100*6+(units-200)*7.5
        print('Bill amount is :  ',bill)
    else:
        print('Meter number does not exist')


while True:
    print("\t\t\t\nElectricity Bill")
    print("1.Enter Customer information")
    print("2.Update Details of a customer")
    print("3.Calculate bill of a customer")
    print("4.exit")
    ch=int(input("Enter your choice:"))
    if(ch==1):
          tc=input("Enter TariffCode LT1/LT2 :")
          cn=input("Enter  Customer Name: ")
          mno=int(input("Enter meter no: "))
          pr=int(input("Enter previous meter reading: "))
          cr=int(input("Enter current meter reading : "))
          if tc=='LT1' or tc=='LT2':
              if cr>pr:
                  insert_rows(tc,cn,mno,pr,cr)
              else:
                  print('Current reading must be greater than previous reading')
          else:
              print('Invalid Tariff Code')

    elif ch==2:
        mno=int(input("Enter meter no: "))
        update_reading(mno)
    elif ch==3:
        mno=int(input("Enter meter no of the customer to calculate bill : "))
        calculate_bill(mno)
    elif ch==4:
        break
    else:
        print('Invalid Choice')



cursor.close()
conn.close()
