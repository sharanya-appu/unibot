import pymysql
def iud(qry,vals) :
    con=pymysql.connect(host="localhost",port=3306,db="chatbot",user="root",passwd="root")
    cur=con.cursor()
    cur.execute(qry,vals)
    id=cur.lastrowid
    con.commit()
    return id
    con.close()
def display(qry,vals) :
    con = pymysql.connect(host="localhost", port=3306, db="chatbot", user="root", passwd="root")
    cur = con.cursor()
    cur.execute(qry,vals)
    s = cur.fetchone()
    con.commit()
    con.close()
    return s

def select(qry) :
    con = pymysql.connect(host="localhost", port=3306, db="chatbot", user="root", passwd="root")
    cur = con.cursor()
    cur.execute(qry)
    s = cur.fetchall()
    con.commit()
    con.close()
    return s


def select1(qry,val) :
    con = pymysql.connect(host="localhost", port=3306, db="chatbot", user="root", passwd="root")
    cur = con.cursor()
    cur.execute(qry,val)
    s = cur.fetchall()
    con.commit()
    con.close()
    return s
