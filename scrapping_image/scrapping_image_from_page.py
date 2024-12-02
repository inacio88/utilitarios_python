import requests
from bs4 import BeautifulSoup
import os
import re

# URL da página que você quer extrair as imagens
url = ""  # Substitua com a URL da página

# Função para baixar as imagens
def baixar_imagem(url_imagem, pasta_destino):
    try:
        # Envia uma requisição para obter a imagem
        resposta = requests.get(url_imagem, stream=True)
        if resposta.status_code == 200:
            # Cria a pasta de destino se não existir
            if not os.path.exists(pasta_destino):
                os.makedirs(pasta_destino)
            # Cria o nome do arquivo a partir da URL
            nome_arquivo = os.path.join(pasta_destino, os.path.basename(url_imagem))
            with open(nome_arquivo, 'wb') as f:
                for pedaço in resposta.iter_content(1024):
                    f.write(pedaço)
            print(f"Imagem salva em {nome_arquivo}")
        else:
            print(f"Falha ao baixar {url_imagem}")
    except Exception as e:
        print(f"Erro ao baixar a imagem {url_imagem}: {e}")

# Função para extrair as URLs das imagens do background
def extrair_imagens(url):
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            # Analisa o conteúdo HTML da página
            soup = BeautifulSoup(resposta.text, 'html.parser')
            # Encontra todas as tags <li> com o estilo que contém as imagens
            li_tags = soup.find_all('li', style=re.compile(r'background-image: url\((.*?)\);'))
            urls_imagens = []
            
            for li in li_tags:
                # Captura a URL da imagem dentro do estilo 'background-image'
                match = re.search(r'url\((.*?)\)', li['style'])
                if match:
                    imagem_url = match.group(1).strip()
                    if imagem_url and imagem_url.startswith('http'):
                        urls_imagens.append(imagem_url)
            
            return urls_imagens
        else:
            print(f"Falha ao acessar a página: {url}")
            return []
    except Exception as e:
        print(f"Erro ao extrair imagens: {e}")
        return []

# Função principal
def main():
    # Extrai todas as URLs das imagens
    urls_imagens = extrair_imagens(url)
    
    # Pasta onde as imagens serão salvas
    pasta_destino = 'imagens_baixadas'
    
    # Baixa todas as imagens
    for imagem_url in urls_imagens:
        baixar_imagem(imagem_url, pasta_destino)

if __name__ == '__main__':
    main()
