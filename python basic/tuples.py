#its like list but tuples value cannot be edited and it uses rounded brackests in place of square in list

tuple=(2,3,5,1,5,)
print(tuple[1])

tuple[1]=2 #not valid 
tup=(1) #not valid it is considerd as integer
tup=(1,) #valid

#practice questions

list =[]
a=input("enter the first movie")
b=input("enter name of second movie")
c=input("enter the name of third movie")
list.append(a)
list.append(b)
list.append(c)
print(list)

l=["r","a","c","e","c","a","r"]
c=l.copy()
c.reverse()
if(l==c):
    print("its a palandrome")
else:
    printa("its not a palandrome")

tup=("c","d","a","a","b","b","a")
print(tup.count("a"))

list=["c","d","a","a","b","b","a"]
list.sort()
print(list)





