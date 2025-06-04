import pandas as pd

def formatar_nomes_viagem(serie):
    """
    Formata nomes de viagem capitalizando corretamente cada palavra, 
    mantendo exceções pré-definidas em minúsculas.
    """
    excecoes = {'de', 'da', 'do', 'dos', 'das', 'e'}
    
    def formatar_nome(nome):
        if pd.isna(nome):
            return nome
            
        palavras = nome.split()
        formatado = []
        for i, palavra in enumerate(palavras):
            if (i > 0) and (palavra.lower() in excecoes):
                formatado.append(palavra.lower())
            else:
                formatado.append(palavra.capitalize())
        return ' '.join(formatado)
    
    return serie.apply(formatar_nome)

def tratar_dataframe(caminho_entrada, caminho_saida, colunas_remover=None):
    """
    Processa um arquivo Excel: importa, trata os dados e exporta para Excel
    """
    try:
        # Importação
        df = pd.read_excel(caminho_entrada)
        print("\nDados importados com sucesso!")
        print(f"Colunas originais: {df.columns.tolist()}")
        
        # Remoção de colunas
        colunas_remover = colunas_remover or []
        colunas_existentes = [col for col in colunas_remover if col in df.columns]
        
        if colunas_existentes:
            df = df.drop(columns=colunas_existentes)
            print(f"Colunas removidas: {colunas_existentes}")
        
        # Formatação de dados
        if 'TRAVEL' in df.columns:
            df['TRAVEL'] = formatar_nomes_viagem(df['TRAVEL'])
            print("Coluna 'TRAVEL' formatada")
        
        if 'PRICE' in df.columns:
            df['PRICE'] = df['PRICE'].apply(
                lambda x: f"R$ {x:,.2f}".replace(',', 'v').replace('.', ',').replace('v', '.') 
                if pd.notnull(x) else x
            )
            print("Coluna 'PRICE' formatada")
        
        # Exportação
        df.to_excel(caminho_saida, index=False)
        print(f"\nArquivo tratado salvo em: {caminho_saida}")
        print(f"Colunas finais: {df.columns.tolist()}")
        
        return df
        
    except Exception as e:
        print(f"\nErro durante o processamento: {str(e)}")
        return None

# Exemplo de uso:
if __name__ == "__main__":
    df_tratado = tratar_dataframe(
        caminho_entrada='/content/arquivodeteste.xlsx',
        caminho_saida='/content/arquivo_tratado.xlsx',
        colunas_remover=['TICKET']
    )
    
    if df_tratado is not None:
        print("\nVisualização do DataFrame tratado:")
        print(df_tratado.head())