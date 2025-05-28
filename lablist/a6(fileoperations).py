f=open('pythonfile.txt','w')
f.writelines(['hellow','let me begin here\n','welcome to python programming by shreevatsa\n'])
f.close()
lcount=0
wcount=0
ccount=0
with open('pythonfile.txt','r') as f:
    print('file contents are')
    for line in f:
        print(line,end='')
        lcount+=1
        wcount+=len(line.split())
        ccount+=len(line.strip())
print(f'\n\nNumber of lines in the file: {lcount}')
print(f'Number of words in the file: {wcount}')
print(f'Number of characters in the file: {ccount}')