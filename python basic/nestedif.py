age =int(input("enter age :"))
if(age >= 18):
    if(age >= 80):
        print("can't drive")
    else:
        print("candrive")
else:
    print("can't drive")

#practice questions

num=int(input("enter a number :"))
if(num%2 == 0):
    print ("even")
else:
    print("odd")

nm1=int(input("enter first number :"))
nm2=int(input("enter second number :"))
nm3=int(input("enter third number :"))
if(nm1>nm2 and nm1>nm3):
    print(nm1)
elif(nm2>nm1 and nm2>nm3):
    print(nm2)
else:
    print(nm3)

num =int(input("enter the number :"))
if(num%7 ==0):
    print("it's divisible by 7")
else:
    print("it's not devisible by 7")
