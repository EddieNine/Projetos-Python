import re
from collections import Counter
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

# Baixar dados necessários para análise de sentimento
nltk.download('vader_lexicon')


def limpar_texto(texto):
    texto = texto.lower()
    texto = re.sub(r'[^\w\s]', '', texto)  # Remove pontuação
    return texto


def contar_palavras(texto):
    palavras = texto.split()
    return len(palavras)


def frequencia_palavras(texto):
    palavras = texto.split()
    return Counter(palavras)


def contar_frases(texto):
    frases = re.split(r'[.!?]', texto)
    frases = [frase.strip() for frase in frases if frase.strip()]
    return len(frases)


def palavras_mais_comuns(texto, n=5):
    freq = frequencia_palavras(texto)
    return freq.most_common(n)


def analisar_sentimento(texto):
    sia = SentimentIntensityAnalyzer()
    sentimento = sia.polarity_scores(texto)
    return sentimento


def main():
    texto = input("Digite ou cole o texto para análise:\n")

    texto_limpo = limpar_texto(texto)

    print(f'\nContagem total de palavras: {contar_palavras(texto_limpo)}')
    print(f'Contagem total de frases: {contar_frases(texto)}')

    print('znFrequnência de palavras:')
    for palavra, freq in frequencia_palavras(texto_limpo).items():
        print(f'{palavra}: {freq}')

    print('\nPalavras mais comuns:')
    for palavra, freq in palavras_mais_comuns(texto_limpo):
        print(f'{palavra}: {freq}')

    sentimento = analisar_sentimento(texto)
    print("\nAnálise de Sentimento:")
    print(f"Positivo: {sentimento['pos']}")
    print(f"Neutro: {sentimento['neu']}")
    print(f"Negativo: {sentimento['neg']}")
    print(f"Composto: {sentimento['compound']}")


if __name__ == "__main__":
    main()
