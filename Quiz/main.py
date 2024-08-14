import threading
import time
import sys


def criar_perguntas():
    # Lista de perguntas e respostas
    perguntas = [
        {
            "pergunta": "Qual componente da inteligência emocional pode ajudar a melhorar "
                        "a eficácia da comunicação em uma equipe? ",
            "opcoes": ["A) Empatia",
                       "B) Motivação",
                       "C) Autocontrole Emocional",
                       "D) Autoconhecimento Emocional"],
            "resposta_correta": 0,
            "feedback": "Empatia pode ajudar a melhorar a eficácia da comunicação em uma equipe, "
                        "pois permite entender melhor as perspectivas e sentimentos dos colegas, "
                        "facilitando uma comunicação mais clara e eficaz."
        },
        {
            "pergunta": "Qual componente da inteligência emocional é fundamental para construir relacionamentos "
                        "fortes e cooperativos, além de comunicar-se de maneira eficaz?",
            "opcoes": ["a) Autocontrole Emocional",
                       "b) Habilidades Sociais",
                       "c) Motivação",
                       "d) Autoconhecimento Emocional"],
            "resposta_correta": 1,
            "feedback": "Habilidades Sociais são fundamentais para construir relacionamentos "
                        "fortes e cooperativos e comunicar-se de maneira eficaz."
        },
        {
            "pergunta": "Qual componente da inteligência emocional está relacionado à capacidade de canalizar emoções "
                        " para alcançar metas e manter uma atitude positiva diante dos desafios?",
            "opcoes": ["a) Autoconhecimento Emocional",
                       "b) Habilidades Sociais",
                       "c) Empatia",
                       "d) Motivação"],
            "resposta_correta": 3,
            "feedback": "Motivação é a capacidade de canalizar emoções "
                        "para alcançar metas e manter uma atitude positiva diante dos desafios."
        },
    ]
    return perguntas


def exibir_pergunta(pergunta_atual, numero, tempo_limite):
    print(f'\nPergunta {numero + 1}: {pergunta_atual['pergunta']}')
    for i, opcao in enumerate(pergunta_atual["opcoes"]):
        print(f'{i}. {opcao}')

    # Variável que armazenará a resposta do usuário
    resposta = [-1]  # Usando uma lista para modificar o valor dentro da função interna

    # Função que será executada após o tempo limite
    def tempo_excedido():
        print('\nTempo esgotado! Nenhum feedback será fornecido para esta pergunta.')
        resposta[0] = -1  # Indica que o tempo acabou sem resposta

    # Criação do temporizador
    timer = threading.Timer(tempo_limite, tempo_excedido)
    timer.start()

    def mostrar_contagem():
        for t in range(tempo_limite, 0, -1):
            sys.stdout.write(f'\rTempo restante: {t} segundos...  ')
            sys.stdout.flush()
            time.sleep(1)
        sys.stdout.write('\r                      \r')  # Limpa a linha depois da contagem

    contagem_thread = threading.Thread(target=mostrar_contagem)
    contagem_thread.start()

    # Captura a resposta do usuário
    resposta_input = int(input('\rDigite o número da sua resposta antes do tempo acabar: '))
    try:
        resposta[0] = int(resposta_input)
    except ValueError:
        resposta[0] = -1  # Resposta inválida

    timer.cancel()  # Cancela o cronômetro se a resposta for dada antes do tempo
    contagem_thread.join()  # Espera a thread de contagem terminar

    return resposta[0]


def verificar_resposta(pergunta, resposta):
    return resposta == pergunta["resposta_correta"]


def mostrar_feedback(pergunta, acertou):
    if acertou:
        print('Correto!')
    else:
        print('Errado!')
    print(f'Explicação: {pergunta['feedback']}')


def main():
    perguntas = criar_perguntas()
    pontuacao = 0
    tempo_limite = 10  # Definindo um limite de 10 segundos por pergunta

    for i, pergunta in enumerate(perguntas):
        resposta = exibir_pergunta(pergunta, i, tempo_limite)
        if resposta != -1:  # Só mostra feedback se a resposta foi dada a tempo
            acertou = verificar_resposta(pergunta, resposta)
            mostrar_feedback(pergunta, acertou)
            if acertou:
                pontuacao += 1
        else:
            print('Pergunta considerada errada devido ao tempo esgotado.')

    print(f'\nSua pontuação final foi: {pontuacao}/{len(perguntas)}')


if __name__ == "__main__":
    main()
