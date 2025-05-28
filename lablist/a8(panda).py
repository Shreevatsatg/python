import pandas as pd
data1={
    'rollno':[1,2,3],
    'name':['shreevatsa','siddharth','siddharth'],
    'marks':[100,200,300]   
}
data2={
    'rollno':[4,5,6],
    'name':['shreevatsa','siddharth','siddharth'],
    'marks':[400,500,600]   
}
df1=pd.DataFrame(data1)
df2=pd.DataFrame(data2)
result=pd.concat([df1,df2],ignore_index=True)
print(result)