from pytube import YouTube
from pytube.exceptions import RegexMatchError, VideoUnavailable


def baixar_video(url, caminho_destino):
    try:
        # Cria um objeto Youtube com a URL do vídeo
        video = YouTube(url)

        # Escolhe a melhor qualidade do vídeo disponível
        stream = video.streams.get_highest_resolution()

        # Faz o download do vídeo para o caminho especificado
        stream.download(output_path=caminho_destino)

        print("Download concluído com sucesso!")
    except RegexMatchError:
        print("Erro: URL inválida")
    except VideoUnavailable:
        print("Erro: Video não está disponivel.")
    except Exception as e:
        print(f'Ocorreu um erro: {e}')


# Exemplo de uso
url_do_video = 'https://www.youtube.com/watch?v=8KCuHHeC_M0'
caminho_destino = 'BaixarVideos/Videos'
baixar_video(url_do_video, caminho_destino)
