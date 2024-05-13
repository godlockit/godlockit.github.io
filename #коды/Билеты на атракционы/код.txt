from datetime import datetime
af = "31.03.2023"
fmt = "%d.%m.%Y"
fd =datetime.now().strftime(fmt)
a = "tit.txt"
i = 1
ticket=[]



while True:
    person_chese = int(input("Выбереит действие 1-купить билеты/2- посмотреть атракционы/3-выйти"))
    if person_chese == 1:
        person_old = int(input("Введите возраст"))
        if person_old < 18:
            atrakt = {"Карусель": 100,"Американские горки":250}
        else:
            atrakt = {"Карусель": 300,"Американские горки":500}
        person_date = input("Введите дату на для просмотра атракционов (DD.ММ.YYYY.)")
        if person_date == fd:
            print("сегодня", fd,", работают: карусель")
            buy = int(input("1 - для покупри, 2- для выхода"))
            if buy == 1:
                print("билет куплен")
                atrk = "Карусель"
                cast = atrakt[atrk]
                cast = str(cast)
                i = str(i)
                a = a + i
                i = int(i)

                with open(a,"w",encoding="utf-8") as file:
                    file.writelines("Вашь атракцион: ")
                    file.write(atrk)
                    print("\n", file=file)
                    file.write("Билетом можно воспользоваться только: ")
                    file.writelines(person_date)
                    print("\n", file=file)
                    file.writelines("Стоимость:")
                    file.write(cast)
                    print("\n", file=file)
                    file.writelines("Статус: Оплачен")
                    ticket.append(a)
                    file.close()
                    i += 1



        elif person_date == af:

            atrk = "Американские горки"
            cast = atrakt["Американские горки"]
            cast = str(cast)
            i = str(i)
            a = a + i
            i = int(i)
            print("31.03.2023 работают американские горки")
            with open("tit.txt", "w", encoding="utf-8") as file:
                file.writelines("Вашь атракцион: ")
                file.write(atrk)
                print("\n",file=file)
                file.write("Билетом можно воспользоваться только: ")
                file.writelines(person_date)
                print("\n",file=file)
                file.writelines("Стоимость:")
                file.write(cast)
                print("\n",file=file)
                file.writelines("Статус: Оплачен")
                ticket.append(a)
                file.close()
                i += 1

    elif person_chese == 3:
        person_old = int(input("Введите возраст"))
        if person_old < 18:
            atrakt = {"Карусель": 100, "Американские горки": 250}
        else:
            atrakt = {"Карусель": 300, "Американские горки": 500}
        print(atrakt)
        print(fd, "-Карусель","")
        while True:
            person_chese2 = int(input("Воспользоваться билетом? (1), выйти(0)"))
            if person_chese == 1:
                print(ticket)
                with open(a, "r", encoding="utf-8") as f:
                    f.seek(139)
                    tit = f.read(10)

                    f.close()
                if tit == fd:
                    print("Билет использован")
                else:
                    print("Билет не использован")
                    print("Билет куплнен на другую дату:",person_date)
            elif person_chese2 == 0:
                break
    elif person_chese == 0 or person_chese == 3:
        print("ПОКА")
        break















