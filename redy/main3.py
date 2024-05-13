def transliterate_back(text):
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

    transliterated_text = ''
    i = 0
    while i < len(text):
        if i+1 < len(text) and text[i:i+2] in translit_dict:
            transliterated_text += translit_dict[text[i:i+2]]
            i += 2
        elif text[i] in translit_dict:
            transliterated_text += translit_dict[text[i]]
            i += 1
        else:
            transliterated_text += text[i]
            i += 1

    return transliterated_text

input_text = "sovremenniy mir !"
output_text = transliterate_back(input_text)
print(output_text)