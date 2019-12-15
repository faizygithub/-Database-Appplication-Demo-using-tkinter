import sqlite3

class Database:
    def connect():
        conn=sqlite3.connect("books.db")
        cur=conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY,title text,auther text,year integer,isbn integer)")
        conn.commit()
        conn.close()

    def insert(title,auther,year,isbn):
        conn=sqlite3.connect("books.db")
        cur=conn.cursor()
        cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title,auther,year,isbn))
        conn.commit()
        conn.close()

    def View():
        conn=sqlite3.connect("books.db")
        cur=conn.cursor()
        cur.execute("SELECT * FROM book ")
        rows=cur.fetchall()
        conn.close()
        return rows
    def search(title="",auther="",year="",isbn=""):
        conn=sqlite3.connect("books.db")
        cur=conn.cursor()
        cur.execute("SELECT * FROM book WHERE title=? OR auther=? OR year=? OR isbn=? ",(title,auther,year,isbn))
        rows=cur.fetchall()
        conn.close()
        return rows


    def delete(id):
        conn=sqlite3.connect("books.db")
        cur=conn.cursor()
        cur.execute("DELETE FROM book WHERE id=?",(id,))
        conn.commit()
        conn.close()

    def update(id,title,auther,year,isbn):
        conn=sqlite3.connect("books.db")
        cur=conn.cursor()
        cur.execute("UPDATE book SET title=?,auther=?,year=?,isbn=? WHERE id=?",(title,auther,year,isbn,id))
        conn.commit()
        conn.close()


    connect()
    #insert("The moon","Jhon smith",1938,98453673)
    #delete(4)
    #update(7," The mars","Jhon deng",2000,98755)
    #print(View())
    #print(search(auther="Jhon smith"))
