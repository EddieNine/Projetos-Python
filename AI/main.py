import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL do site que deseja coletar dados
url = "https://g1.globo.com/"

# Faz a requisição para a página
response = requests.get(url)

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    # Faz o parsing do conteúdo HTML
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encontra as manchetes
    headlines = soup.find_all('a', class_='feed-post-link')

    # Coleta as manchetes e os links
    news_data = []
    for headline in headlines:
        title = headline.get_text().strip()
        link = headline['href']
        news_data.append({'Título': title, 'Link': link})

    # Converte para DataFrame para melhor visualização
    df = pd.DataFrame(news_data)

    # Exibe as manchetes coletadas
    print(df)
else:
    print("Erro ao acessar o site")

# Salva os dados em um arquivo CSV
df.to_csv('manchetes.csv', index=False)
print("Manchetes salvas no arquivo 'manchetes.csv'.")