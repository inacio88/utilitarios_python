import pandas as pd

def process_excel_file(file_path, num_times):
    # Lê o arquivo Excel
    excel_file = pd.ExcelFile(file_path)
    
    # Processa cada folha
    for sheet_name in excel_file.sheet_names:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        
        # Verifica se há pelo menos 1 linha na folha
        if len(df) < 1:
            print(f"A folha '{sheet_name}' não tem pelo menos 1 linha. Pulando...")
            continue
        
        # Copia a primeira linha
        first_row = df.iloc[0]
        
        # Cria um DataFrame com as linhas a serem adicionadas
        rows_to_add = pd.DataFrame([first_row] * num_times, columns=df.columns)
        
        # Anexa as novas linhas ao DataFrame original
        df_updated = pd.concat([df, rows_to_add], ignore_index=True)
        
        # Salva as alterações na folha
        with pd.ExcelWriter(file_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
            df_updated.to_excel(writer, sheet_name=sheet_name, index=False)
        
        print(f"Processado a folha '{sheet_name}'.")

# Solicita ao usuário o caminho do arquivo e o número de vezes para duplicar a linha
# file_path = input("Digite o caminho do arquivo Excel (.xlsx): ")
# num_times = int(input("Digite o número de vezes para duplicar a primeira linha: "))
# python3 -m venv ambiente
file_path = "teste2.xlsx"
num_times = 10000
# Processa o arquivo Excel
process_excel_file(file_path, num_times)
