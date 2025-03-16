t1=(1,2,5,7,9,2,4,6,8,10)
t2=(11,13,15)
t3=()
list1=[]
while True:
    print("\n1.Print half of the tuple in one line and rest of the half tuple in another line")
    print("2.Print even tuple from given tuple")
    print("3.Concatinate the tuple t2=(11,13,15) with t1")
    print("4.Return max and min values from the tuple")
    print("5.Exit")
    ch=int(input("Enter your choice: "))
    if ch==1:
        half=len(t1)//2
        print(t1[:half])
        print(t1[half:])
    elif ch==2:
        for n in t1:
            if n%2==0:
                list1.append(n)
        t3=tuple(list1)
        print("Even Tuple",t3)
    elif ch==3:
        print("Concatination of tuples")
        t1=t1+t2
        print(t1)
    elif ch==4:
        print("Maximum: ",max(t1))
        print("Minimum: ",min(t1))
    elif ch==5:
        break
    else:
        print("Invalid Choice")
        
