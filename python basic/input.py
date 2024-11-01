name =input("name :")
print( name )
sname = str(input('name:'))

name=input("emter your name") #by default all inouts are string
print("welcome",name)

num1=int(input("enter a number")) #considersd as integer
num2=input("enter a second nymber")#considered as string
print(type(num1))
print(type(num2))

a =float(input("enter 1st number"))
b =float(input("enter second number"))
c=(a+b)/2
print(c)

a=int(input("enter the a value :"))
b=int(input("enter the b value :"))
if(a>=b):
    c=True
else:
    c=False
print(c)
