def nearly_equal(s1,s2):
    if len(s1) != len(s2):
        return False
    count=0
    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            count+=1
    return count==1

s1=input('enter first string: ')
s2=input('enter second string: ')
if s1==s2:
    print('strings are equal')
elif nearly_equal(s1,s2):
    print('strings are nearly equal')
else:
    print('strings are not equal')