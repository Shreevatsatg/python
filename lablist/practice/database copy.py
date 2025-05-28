import mysql.connector 
conn=mysql.connector.connect(host='localhost',database='Sample',user='root', password='',buffered=True) 
cursor=conn.cursor() 
 
def insert_rows(ano,btitle,pc):     
    st="select * from book where accno='%d'"     
    arg=(ano)     
    cursor.execute(st % arg)     
    if cursor.rowcount>=1: 
        print("book with same accno exists") 
    else: 
        st="insert into book values('%d','%s','%f')"         
        arg=(ano,btitle,pc)         
        cursor.execute(st % arg)         
        conn.commit()         
        print('1 Row inserted........') 
     
def display_specific(ano):     
    st="select * from book where accno='%d'"     
    arg=(ano)     
    cursor.execute(st % arg)     
    if cursor.rowcount>0:         
        row=cursor.fetchone()         
        print(f'\nAccession no : {row[0]}, Title : {row[1]}, Price : {row[2]}') 
    else: 
        print('Book does not exist') 
 
def display_all():     
    cursor.execute("select * from book")     
    if cursor.rowcount>0:         
        rows=cursor.fetchall()         
        print('\nBooks List ')         
        print('Accno\t\tTitle\t\tPrice')         
        for row in rows: 
            print(f'{row[0]}\t\t{row[1]}\t\t{row[2]}') 
    else: 
        print('No books found') 
     
def display_range(low,high):     
    st="select * from book where price between '%f' and '%f'"     
    arg=(low,high)     
    cursor.execute(st % arg)     
    if cursor.rowcount>=1:         
        rows=cursor.fetchall()         
        print('\nBooks within the given range are')         
        print('Accno\t\tTitle\t\tPrice')         
        for row in rows: 
            print(f'{row[0]}\t\t{row[1]}\t\t{row[2]}') 
    else: 
        print("No books found in that price range") 
 
def delete_specific(ano):     
    st="delete from book where accno='%d'"     
    arg=(ano) 
    cursor.execute(st % arg)     
    if cursor.rowcount>0:         
        print('Book deleted') 
    else: 
        print('Book does not exist') 
    
if __name__=='__main__': 
    while True: 
        print('\n----------------------------------------------') 
        print("\tBook Information Menu")         
        print("1.Enter book information")         
        print("2.Display details of specific book")         
        print("3.Display book where price lies within a certain range")         
        print("4. Display details of all books")         
        print("5. Delete a book")               
        print("6.exit")         
        print('-----------------------------------------------') 
        ch=int(input("Enter your choice:"))         
        if(ch==1): 
            n=int(input("How many books")) 
            for i in range(n): 
                ano=int(input("Enter accno:"))                 
                btitle=input("Enter  book title:")                 
                pc=float(input("Enter price:"))                 
                insert_rows(ano,btitle,pc)         
        elif ch==2: 
            ano=int(input("Enter accession no:")) 
            display_specific(ano)         
        elif ch==3: 
            low=float(input("Enter lower range of price : "))             
            high=float(input("Enter upper range of price : "))             
            display_range(low,high)         
        elif ch==4: 
            display_all()         
        elif ch==5: 
            ano=int(input("Enter accession no: of the book to delete"))             
            delete_specific(ano)         
        elif ch==6:             
            break         
        else: 
            print('Invalid Choice') 
 
cursor.close()
conn.close() 
