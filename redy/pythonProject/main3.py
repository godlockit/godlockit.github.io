
translit_dict = {
        'a': 'а', 'b': 'б', 'c': 'с', 'd': 'д', 'e': 'е',
        'f': 'ф', 'g': 'г', 'h': 'х', 'i': 'и', 'j': 'ж',
        'k': 'к', 'l': 'л', 'm': 'м', 'n': 'н', 'o': 'о',
        'p': 'п', 'q': 'к', 'r': 'р', 's': 'с', 't': 'т',
        'u': 'у', 'v': 'в', 'w': 'в', 'x': 'кс', 'y': 'й',
        'z': 'з',
        'A': 'А', 'B': 'Б', 'C': 'С', 'D': 'Д', 'E': 'Е',
        'F': 'Ф', 'G': 'Г', 'H': 'Х', 'I': 'И', 'J': 'Ж',
        'K': 'К', 'L': 'Л', 'M': 'М', 'N': 'Н', 'O': 'О',
        'P': 'П', 'Q': 'К', 'R': 'Р', 'S': 'С', 'T': 'Т',
        'U': 'У', 'V': 'В', 'W': 'В', 'X': 'Кс', 'Y': 'Й',
        'Z': 'З'
    }
translit_dict2 = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd',
        'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
        'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n',
        'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
        'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch',
        'ш': 'sh', 'щ': 'sch', 'ъ': '', 'ы': 'y', 'ь': '',
        'э': 'e', 'ю': 'yu', 'я': 'ya',
        'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D',
        'Е': 'E', 'Ё': 'Yo', 'Ж': 'Zh', 'З': 'Z', 'И': 'I',
        'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N',
        'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T',
        'У': 'U', 'Ф': 'F', 'Х': 'Kh', 'Ц': 'Ts', 'Ч': 'Ch',
        'Ш': 'Sh', 'Щ': 'Sch', 'Ъ': '', 'Ы': 'Y', 'Ь': '',
        'Э': 'E', 'Ю': 'Yu', 'Я': 'Ya'
    }

def vrus(text):
    text1 = ''
    i = 0
    while i < len(text):
        if i + 1 < len(text) and text[i:i + 2] in translit_dict:
            text1 += translit_dict[text[i:i + 2]]
            i += 2
        elif text[i] in translit_dict:
            text1 += translit_dict[text[i]]
            i += 1
        else:
            text1 += text[i]
            i += 1

    return text1  # рус


def vangl(text):
    text2 = ''
    for char in text:
        if char in translit_dict:
            text2 += translit_dict[char]
        else:
            text2 += char

    return text2 #ванг

