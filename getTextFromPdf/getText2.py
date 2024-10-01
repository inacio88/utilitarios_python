import fitz  # Módulo principal do PyMuPDF

# Abre o arquivo PDF
pdf_document = fitz.open("chili.pdf")

# Itera sobre cada página do PDF
for page_index in range(len(pdf_document)):
    page = pdf_document[page_index]
    text = page.get_text()
    print(text)

# Fecha o documento PDF
pdf_document.close()