import sqlite3

class Database:

    def __init__(self,db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY,title text,auther text,year integer,isbn integer)")
        self.conn.commit()


    def insert(self,title,auther,year,isbn):
        self.conn=sqlite3.connect("books.db")
        self.cur=self.conn.cursor()
        self.cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title,auther,year,isbn))
        self.conn.commit()


    def View(self):
        self.cur.execute("SELECT * FROM book ")
        rows=self.cur.fetchall()
        return rows
    def search(self,title="",auther="",year="",isbn=""):
        self.cur.execute("SELECT * FROM book WHERE title=? OR auther=? OR year=? OR isbn=? ",(title,auther,year,isbn))
        rows=self.cur.fetchall()
        return rows


    def delete(self,id):
        self.cur.execute("DELETE FROM book WHERE id=?",(id,))
        self.conn.commit()


    def update(self,id,title,auther,year,isbn):
        self.cur.execute("UPDATE book SET title=?,auther=?,year=?,isbn=? WHERE id=?",(title,auther,year,isbn,id))
        self.conn.commit()
    def __del__():
        self.conn.close()    




#insert("The moon","Jhon smith",1938,98453673)
#delete(4)
#update(7," The mars","Jhon deng",2000,98755)
#print(View())
#print(search(auther="Jhon smith"))
