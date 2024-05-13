def compare_rus_eng(rus, eng):
    rus = rus.lower()
    eng = eng.lower()
    translit = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'sch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
    if len(rus) != len(eng):
        return False
    for i in range(len(rus)):
        if rus[i] in translit:
            if translit[rus[i]] != eng[i]:
                return False
        else:
            return False
    return True

print(compare_rus_eng("Пт", "Privet"))