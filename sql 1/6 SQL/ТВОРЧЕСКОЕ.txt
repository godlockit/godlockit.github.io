

import sqlite3

con = sqlite3.connect('tovar4DB.db')
cursor = con.cursor()
try:

    cursor.execute(
        "CREATE TABLE tovar (id INTEGER PRYMARY KEY AUTOINCOREMENT,name TEXT,qual INTEGER ,cost INTEGER,sum_tovarov INTEGER)"
    )
except:
    pass
while True:
    persondata = int(input("Введите номер действия: 1-добавить продукт 2-вызвать таблицу 3-Удаление товара 4-Изменение количества товара 5-сумма стоимости всего товара :"))
    if persondata == 1:
        name = input('name:')
        qual = int(input('qual:'))
        cost = int(input('cost:'))
        cursor.execute(f"INSERT INTO tovar (name,qual,cost) VALUES ('{name}','{qual}',{cost})")
        con.commit()
    elif persondata ==2:
        cursor.execute("SELECT * FROM tovar")
        tovar = cursor.fetchall()
        for i in range(len(tovar)):
            print(f"id: {tovar[i][0]} name:{tovar[i][1]} qual:{tovar[i][2]} ,cost :{tovar[i][3]},sum_tovarov:{tovar[i][4]} ")
    elif persondata == 4:
        persondata = int(input("Введите чило действия: 1-напрямую изменить колличество 2-Увеличить или уменьшить количество :"))
        if persondata == 1:
            persondata = int(input("Введите id товара для изменения колличества"))
            id = persondata
            persondata = int(input('Введите qual :'))
            cursor.execute(f"UPDATE tovar set qual = {persondata} WHERE id={id}")
        elif persondata == 2:
            persondata = int(input("Введите id товара для изменения колличества"))
            id=persondata
            persondata = input("Увеличить (+) или уменьшить (-) количество : ")
            if persondata == '+':
                cursor.execute(f"UPDATE tovar set qual = qual+{1} WHERE id={id}")
    elif persondata == 3:
        if persondata == 1:
            persondata = int(input("Введите id товара для удаления"))
            cursor.execute(f"DELETE FROM tovar WHETE id ={persondata}")
    elif persondata == 5:
        persondata = int(input("1-по ид 2- вся"))

        if persondata == 2:
            cursor.execute("SELECT * FROM tovar")
            tovar = cursor.fetchall()
            sumall2 = 0
            for i in range(len(tovar)):
                sumall = tovar[i][2] * tovar[i][3] + sumall2
                sumall2 = sumall
            print(sumall)

        elif persondata == 1:
            persondata = int(input("Введите ид"))
            i = persondata
            cursor.execute("SELECT * FROM tovar")
            tovar = cursor.fetchall()
            sumall = tovar[i][2] * tovar[i][3]
            print(sumall)



    if persondata == 0:
        break





