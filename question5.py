def inverter_string(string):
    tamanho = len(string)
    string_invertida = ""
    for i in range(tamanho - 1, -1, -1):
        string_invertida += string[i]
    return string_invertida

entrada = input("Digite uma string: ")
print("String original:", entrada)
print("String invertida:", inverter_string(entrada))
