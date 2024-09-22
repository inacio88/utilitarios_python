import requests
from bs4 import BeautifulSoup
import time
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def extract_text_from_p_tags(url):
    """Extrai o texto de todas as tags <p> dentro de divs com a classe especificada.

    Args:
        url (str): URL da página da web.

    Returns:
        list: Uma lista contendo o texto extraído de cada tag <p>.
    """

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encontrar todas as divs com a classe especificada
    divs = soup.find_all('div', class_='col-xs-12 col-md-8 card')

    text_list = []
    for div in divs:
        # Encontrar todas as tags <p> dentro da div
        paragraphs = div.find_all('p')
        for paragraph in paragraphs:
            elementos = paragraph.contents
            for text in elementos:
                condicao = text.name == 'br'
                if ( not condicao):
                    text_list.append(text)

    return text_list

for i in alfabeto:
    for j in alfabeto:
        url = f"https://www.dicio.com.br/palavras-comecam-{i}{j}"
        print(url)

        time.sleep(5)

        texts = extract_text_from_p_tags(url)
        if (len(texts) > 2):
            texts.pop(0)
            texts.pop()
        if (len(texts) > 0):
            texts[0] = texts[0].replace('\n                ', "")
        for text in texts:
            print("\n")
            print(text)


        with open(f"palavras_{i}{j}.txt", "w") as file:
            for c in texts:
                file.write(''.join(c) + "\n")