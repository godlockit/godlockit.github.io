#Шакуро Илья


import sqlite3

con = sqlite3.connect('peson2DB.db')
cursor = con.cursor()
try:

    cursor.execute(
        "CREATE TABLE person (id INTEGER PRYMARY KEY AUTOINCOREMENT,name TEXT,email TEXT ,hours INTEGER, itemPerHours INTEGER)"
    )
except:
    pass
name1 = "kit1"
email1 = "kit1@mail.ru"
hours1 = 2
itemPerHours1 = 23

name2 = "kit2"
email2 = "kit2@mail.ru"
hours2 = 4
itemPerHours2 = 16

name3 = "kit3"
email3 = "kit3@mail.ru"
hours3 = 1
itemPerHours3 = 10

cursor.execute("DELETE FROM person")

cursor.execute(f"INSERT INTO person (name,email,hours,itemPerHours) VALUES ('{name1}','{email1}',{hours1},{itemPerHours1})")
cursor.execute(f"INSERT INTO person (name,email,hours,itemPerHours) VALUES ('{name2}','{email2}',{hours2},{itemPerHours2})")
cursor.execute(f"INSERT INTO person (name,email,hours,itemPerHours) VALUES ('{name3}','{email3}',{hours3},{itemPerHours3})")
cursor.execute(f"INSERT INTO person (name,email,hours,itemPerHours) VALUES ('{name1}','{email3}',{hours2},{itemPerHours1})")
cursor.execute(f"INSERT INTO person (name,email,hours,itemPerHours) VALUES ('{name2}','{email1}',{hours3},{itemPerHours2})")
cursor.execute(f"INSERT INTO person (name,email,hours,itemPerHours) VALUES ('{name1}','{email1}',{hours1},{itemPerHours1})")
cursor.execute(f"INSERT INTO person (name,email,hours,itemPerHours) VALUES ('{name2}','{email2}',{hours2},{itemPerHours2})")
cursor.execute(f"INSERT INTO person (name,email,hours,itemPerHours) VALUES ('{name3}','{email3}',{hours3},{itemPerHours3})")
cursor.execute(f"INSERT INTO person (name,email,hours,itemPerHours) VALUES ('{name1}','{email3}',{hours2},{itemPerHours1})")
cursor.execute(f"INSERT INTO person (name,email,hours,itemPerHours) VALUES ('{name2}','{email1}',{hours3},{itemPerHours2})")
con.commit()

cursor.execute("SELECT * FROM person WHERE hours*itemPerHours > 14")
person = cursor.fetchall()

name = person[1][1]
for i in range(len(person)):

    print(f"id: {person[i][0]} name:{person[i][1]} email:{person[i][2]} ")

#id – число, первичный ключ, автоматическое увеличение
#name – текст
#email – текст
#hours – число
#itemsPerHours – число
