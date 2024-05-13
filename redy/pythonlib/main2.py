import lib2

text = input("Введите текст")
person = int(input("Выбирите действие 1-количество букв, 2-количество слов,3-количество предложений"))
if person == 1:
    ww=lib2.wordcross.count_simvol(text)
    print(ww)
if person == 2:
    ww = lib2.wordcross.count_words(text)
    print(ww)
if person == 3:
    ww = lib2.wordcross.count_pred(text)
    print(ww)


