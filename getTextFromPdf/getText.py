import PyPDF2

def extract_text_to_txt(pdf_file, txt_file):
    """Extrai o texto de um PDF e salva em um arquivo TXT.

    Args:
        pdf_file (str): Caminho para o arquivo PDF.
        txt_file (str): Caminho para o arquivo TXT de saída.
    """

    with open(pdf_file, 'rb') as pdf_reader:
        reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()

    with open(txt_file, 'w', encoding='utf-8') as txt_writer:
        txt_writer.write(text)

# Exemplo de uso:
pdf_path = "GS248-GettingStarted.pdf"
txt_path = "texto_extraido.txt"
extract_text_to_txt(pdf_path, txt_path)