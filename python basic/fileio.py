# f=open("python basic/loops.py","r") #("file location","opening type r:read or w:write")
# data =f.read()
# print(data)
# f.close()

# f=open("python basic/fileioex.txt")
# data =f.read(10)       #number of charecter to read and readline is used to read a single line
# print(data)


# f = open("python basic/fileioex.txt","w")
# data = f.write("this is after useing write command to override the present text in the file")   
# print(data)
# f.close()

# #syntax with
# with open("python basic/fileioex.txt","r") as f:
#     data = f.read()
#     print(data)

# import os #provides remove file option
# os.remove("python basic/fileioex.txt")      #deletes the file

# with open("practice.txt","r") as f: #if no file exists it will creates a new one by its own
#     data= f.read()
# newdata=data.replace("java","pyhton")
# print(newdata)



