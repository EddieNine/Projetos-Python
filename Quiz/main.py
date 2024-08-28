import time
import os
import msvcrt  # Apenas para Windows


def criar_perguntas():
    perguntas = [
        {
            "pergunta": "Qual componente da inteligência emocional "
                        "pode ajudar a melhorar a eficácia da comunicação em uma equipe?",
            "opcoes":
                ["A) Empatia",
                 "B) Motivação",
                 "C) Autocontrole Emocional",
                 "D) Autoconhecimento Emocional"],
            "resposta_correta": 0,
            "feedback": "Empatia pode ajudar a melhorar a eficácia da comunicação em uma equipe, "
                        "pois permite entender melhor as perspectivas e sentimentos dos colegas, "
                        "facilitando uma comunicação mais clara e eficaz."
        },
        # Outras perguntas...
    ]
    return perguntas


def exibir_pergunta(pergunta_atual, numero, tempo_limite):
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela
    print(f'\nPergunta {numero + 1}: {pergunta_atual["pergunta"]}')
    for i, opcao in enumerate(pergunta_atual["opcoes"]):
        print(f'{i}. {opcao}')

    inicio = time.time()
    resposta = None

    print(f"\nVocê tem {tempo_limite} segundos para responder...")

    while True:
        tempo_decorrido = time.time() - inicio
        tempo_restante = tempo_limite - int(tempo_decorrido)

        if tempo_restante <= 0:
            print('\nTempo esgotado!')
            resposta = -1  # Indicador de tempo esgotado
            break

        # Verifica se uma tecla foi pressionada
        if msvcrt.kbhit():
            resposta = msvcrt.getche().decode('utf-8')
            if resposta.isdigit():
                resposta = int(resposta)
                break
            else:
                resposta = None  # Reinicia a variável para continuar o loop

        print(f"\rTempo restante: {tempo_restante} segundos", end='', flush=True)
        time.sleep(1)

    return resposta


def verificar_resposta(pergunta, resposta):
    return resposta == pergunta["resposta_correta"]


def mostrar_feedback(pergunta, acertou):
    if acertou:
        print('Correto!')
    else:
        print('Errado!')
    print(f'Explicação: {pergunta["feedback"]}')


def main():
    perguntas = criar_perguntas()
    pontuacao = 0
    tempo_limite = 10  # Tempo limite em segundos

    for i, pergunta in enumerate(perguntas):
        resposta = exibir_pergunta(pergunta, i, tempo_limite)
        if resposta != -1:
            acertou = verificar_resposta(pergunta, resposta)
            mostrar_feedback(pergunta, acertou)
            if acertou:
                pontuacao += 1
        else:
            print('Pergunta considerada errada devido ao tempo esgotado.')

    print(f'\nSua pontuação final foi: {pontuacao}/{len(perguntas)}')


if __name__ == "__main__":
    main()
