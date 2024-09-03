import random
import time

computador = random.randint(1, 100)
chances = 10
cont = 0

print("""------ \033[34mBEM-VINDO AO JOGO DA ADIVINHAÇÃO\033[m ------""")
print("\033[36mO Computador está pensando em um número...\033[m ")
time.sleep(2)
while True:
    jogador = int(input("\033[35mTente adivinhar o número de 1 a 100:\033[m "))
    cont += 1

    if jogador > computador:
        print(f'Seu palpite está alto!')
        chances -= 1
        print(f'Você tem {chances} chances restantes')
    elif jogador < computador:
        print('Seu palpite está baixo')
        chances -= 1
        print(f'Você tem {chances} chances restantes')
    else:
        print(f'\033[32mParabéns, você acertou! O número era {computador}.\033[m')
        print(f'Você precisou de {cont} tentativas.')
        break

    if chances == 0:
        print(f'\033[31mSuas chances acabaram! O número correto era {computador}. Boa sorte na próxima vez!\033[m')
        break
