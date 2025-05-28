def sarea(s):
    a=s*s
    print('Area of square : ',a)

def carea(r):
    a=22/7*r*r
    print('Area of circle : ',a)

def rarea(l,b):
    a=l*b
    print('Area of rectangle : ',a)

def tarea(b,h):
    a=1/2*b*h
    print('Area of triangle : ',a)

while True:
    print('\n1. Area of square')
    print('2. Area of circle')
    print('3. Area of rectangle')
    print('4. Area of triangle')
    print('5. Exit')
    ch=int(input('Enter your choice : '))
    if ch==1:
        s=int(input('Enter side : '))
        sarea(s)
    elif ch==2:
        r=int(input('Enter radius : '))
        carea(r)
    elif ch==3:
        l=int(input('Enter length : '))
        b=int(input('Enter breadth : '))
        rarea(l,b)
    elif ch==4:
        b=int(input('Enter base : '))
        h=int(input('Enter heigth : '))
        tarea(b,h)
    elif ch==5:
        break
    else:
        print('Invalid choice')

