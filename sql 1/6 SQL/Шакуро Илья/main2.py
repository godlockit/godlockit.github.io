#Шакуро Илья


import sqlite3
import random

con = sqlite3.connect('peson3DB.db')
cursor = con.cursor()
try:

    cursor.execute(
        "CREATE TABLE person (id INTEGER PRYMARY KEY AUTOINCOREMENT,name TEXT,age INTEGER ,weight INTEGER, height INTEGER, bmi REAL)"
    )
except:
    pass



cursor.execute("DELETE FROM person")

words = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','n','m']
name = ""
for i in range(5):
    name += random.choice(words)

for i in range (1000):
    name = ""
    for v in range(5):
        name += random.choice(words)
    name1 = name
    age1 = random.randint(1,100)
    weight1 = random.randint(50,300)
    height1 = random.randint (100,300)
    bmi1 = weight1/(height1*height1)

    cursor.execute(f"INSERT INTO person (name,age,weight,height,bmi) VALUES ('{name1}','{age1}',{weight1},{height1},{bmi1})")
con.commit()

cursor.execute("SELECT * FROM person WHERE bmi < 20 or bmi > 30")
person = cursor.fetchall()

name = person[1][1]
for i in range(len(person)):

    print(f"id: {person[i][0]} name:{person[i][1]} age:{person[i][2]} , bmi:{person[i][5]} ")


