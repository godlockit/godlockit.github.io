def rost():
    text = input("Введите числа: ")
    numli = list(text)
    sortli = sorted(numli,reverse=True)
    print (''.join(sortli))
rost()