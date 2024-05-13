def caeser_cipher(text,shift):
    result = ""
    for char in text:
        if char.isalpha():
            alphabet = "abcdefghijklmnopqrstuvwxyz"
            upper_case = False
            if char.isupper():
                upper_case = True
                char=char.lower()
                index = alphabet.find(char)
                index = (index+shift)%26
                if upper_case:
                    result += alphabet[index].upper()
                else:
                    result +=alphabet[index]
            else:
                result +=char
    return result

print("Данная программа переводит текс из вашего файла в зашифрованый вариант с помошью шифра цезаря ")
person_index = input("Введите название файла из которово мы будем брать текст для шифровки (______.txt) :")
person_output = input("Введите название файла в который мы будем записывать текст шифровки (______.txt) :")

input_file = open(person_index, "r", encoding="utf-8")
output_file = open(person_output,"w",encoding="utf-8")
shift = 3
text = input_file.read()
cipher_text = caeser_cipher(text,shift)
output_file.write(cipher_text)
input_file.close()
output_file.close()
print("смотрите результат в файле :",person_output,)


