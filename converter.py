import base64
import pandas as pd
import tabula

def base64_para_pdf(arquivo_base64, arquivo_pdf):
    try:
        # Decodificar os dados base64
        arquivo = base64.b64decode(arquivo_base64)

        # Escrever os dados decodificados em um arquivo PDF
        with open(arquivo_pdf, 'wb') as f:
            f.write(arquivo)

        df_combinado = pdf_para_dataframe(arquivo_pdf)
        df_combinado.columns = ['Histórico de Despesas', 'Valor total', 'Unnamed: 0', 'Parcelas', 'Valor mês', 'Encargos']

        df_combinado.to_excel('dados_sem_tratamento.xlsx', index=False)
        df = df_combinado.copy()
        print(df.head(60))
        # df_combinado.columns = ['Histórico de Despesas', 'Valor total', 'Unnamed: 0', 'Parcelas', 'valor mês', 'Encargos']
        df_teste = df.loc[0:11]
        print(df_teste)

        return True, None  # Retorna True (sucesso) e nenhum erro

    except Exception as e:
        return False, str(e)  # Retorna False (falha) e a mensagem de erro
        
def pdf_para_dataframe(arquivo_pdf):
    tabelas = tabula.read_pdf(arquivo_pdf, pages='1-2')
    df_combinado = pd.DataFrame()
    print(df_combinado)
    for tabela in tabelas:
        df = tabela.copy()
        df_combinado = pd.concat([df_combinado, df], ignore_index=True)
    return df_combinado 

# arquivo_pdf = 'fatura01202402.pdf'



