import random
import string


# Definir os caracteres disponíveis
letras_maiusculas = string.ascii_uppercase
letras_minusculas = string.ascii_lowercase
numeros = string.digits
simbolos = string.punctuation

# Definir quais tipos de caracteres serão usados
caracteres = letras_maiusculas + letras_minusculas + numeros + simbolos

# Solicitar o comprimento da senha ao usuário
comprimento = int(input("Qual o comprimento desejado para a senha? "))

# Gerar a senha
senha = ''.join(random.choice(caracteres) for _ in range(comprimento))

print(f'Sua senha gerada é: {senha}')
