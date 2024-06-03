def inverter_string(s):
    # Inicializa uma string vazia para armazenar a string invertida
    string_invertida = ""
    # Percorre a string original de trás para frente
    for char in s:
        # Adiciona cada caractere ao início da string invertida
        string_invertida = char + string_invertida
    return string_invertida

# Exemplo de uso:
string_original = "Olá, mundo!"
string_invertida = inverter_string(string_original)
print(string_original) # Saída: Olá, mundo!
print(string_invertida)  # Saída: !odnum ,álO
