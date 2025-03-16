list1=[]
uniquelist=[]
def unlist(mylist):
    for n in mylist :
        c=mylist.count(n)
        if c==1:
            uniquelist.append(n)
n=int(input("enter the number of elements"))
for i in range(n):
    ele=int(input(f"enter the element{i+1}:"))
    list1.append(ele)
print("the entered list is ",list1)
print("unique list is:",uniquelist)