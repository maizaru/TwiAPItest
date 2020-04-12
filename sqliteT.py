import sqlite3,time

'''
dbName = 'Twitter.db'
conn = sqlite3.connect(dbName)
cur = conn.cursor()

cur.execute('CREATE TABLE DMtables(\
                id       INTEGER PRIMARY KEY AUTOINCREMENT,\
                name     STRING,\
                userId   STRING,\
                content  STRING,\
                sendDate STRING)')
'''

def Execute(userName,userId,textContent):
    dbName = 'Twitter.db'
    conn = sqlite3.connect(dbName)
    cur = conn.cursor()

    sql = 'INSERT INTO DMtables(name,userId,content,sendDate) values(?,?,?,?)'
    values = (userName,userId,textContent,'2014/4/12')#time.time())
    cur.execute(sql,values)

    conn.commit()
    cur.close()
    conn.close()