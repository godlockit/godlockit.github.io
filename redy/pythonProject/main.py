def wordspam():
    text= input("Введите что-то: ")
    af = len(text) - 3
    la = ""
    for char in text:
        if af > 0 and af !=0:
            af = af -1
            char = "#"
            la = la + char
        else:
            la = la + char
    print(la)


wordspam()