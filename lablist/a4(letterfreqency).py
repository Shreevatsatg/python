def fcount(st):
    fq={}
    for x in st:
        if x.isalpha():
            fq[x]=fq.get(x,0)+1
    print(fq)

st=input('Enter a statement : ')
print('Frequencies of letters in string : ')
fcount(st)
