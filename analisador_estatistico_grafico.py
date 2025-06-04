"""
analisador_estatistico_grafico.py

Um script interativo que coleta números, realiza análises estatísticas e gera visualizações gráficas.

Funcionalidades:
1. Coleta números via entrada interativa
2. Calcula estatísticas descritivas (média, mediana, desvio padrão, etc.)
3. Gera múltiplos tipos de gráficos (linha, histograma, boxplot)
4. Permite salvar os gráficos em diferentes formatos
5. Oferece opção para exportar os dados coletados

Autor: Seu Nome
Data: 2023-10-15
Versão: 1.0
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from datetime import datetime

# Configurações de estilo
sns.set(style="whitegrid")
plt.rcParams['font.family'] = 'DejaVu Sans'

def coletar_numeros() -> list:
    """
    Coleta números digitados pelo usuário de forma interativa.
    
    Retorna:
        list: Lista de números fornecidos pelo usuário
    """
    numeros = []
    print("\n" + "="*50)
    print("COLETA DE DADOS".center(50))
    print("="*50)
    print("Digite números (um por linha). Para finalizar, digite:")
    print("  - 'sair': Termina a coleta")
    print("  - 'exportar': Mostra opções de exportação")
    print("  - 'help': Mostra esta mensagem novamente")
    print("\nDica: Você pode colar múltiplos valores de uma vez!")
    print("="*50)
    
    while True:
        entrada = input("Número: ").strip()
        
        if entrada.lower() == 'sair':
            break
            
        if entrada.lower() == 'exportar':
            exportar_dados(numeros)
            continue
            
        if entrada.lower() in ['help', 'ajuda']:
            print("\nComandos disponíveis:")
            print("  sair     - Termina a coleta de dados")
            print("  exportar - Exporta os dados coletados")
            print("  help     - Mostra esta ajuda")
            continue
            
        try:
            num = float(entrada)
            numeros.append(num)
            print(f"✓ Adicionado: {num}")
        except ValueError:
            print(f"Entrada ignorada: '{entrada}' não é um número válido")
    
    return numeros

def calcular_estatisticas(dados: list) -> dict:
    """
    Calcula estatísticas descritivas para uma lista de números.
    
    Parâmetros:
        dados (list): Lista de valores numéricos
        
    Retorna:
        dict: Dicionário com várias métricas estatísticas
    """
    if not dados:
        return {}
    
    arr = np.array(dados)
    return {
        'n': len(arr),
        'média': np.mean(arr),
        'mediana': np.median(arr),
        'desvio_padrão': np.std(arr),
        'variância': np.var(arr),
        'mínimo': np.min(arr),
        'máximo': np.max(arr),
        'percentil_25': np.percentile(arr, 25),
        'percentil_75': np.percentile(arr, 75),
        'amplitude': np.ptp(arr)
    }

def exibir_estatisticas(estatisticas: dict):
    """
    Exibe estatísticas formatadas em uma tabela.
    
    Parâmetros:
        estatisticas (dict): Dicionário de estatísticas
    """
    if not estatisticas:
        print("\nNenhum dado para analisar!")
        return
    
    print("\n" + "="*50)
    print("ANÁLISE ESTATÍSTICA".center(50))
    print("="*50)
    
    for key, value in estatisticas.items():
        # Formata valores float para 2 casas decimais
        formatted_value = f"{value:.4f}" if isinstance(value, float) else value
        # Substitui underscores por espaços e capitaliza
        formatted_key = key.replace('_', ' ').capitalize()
        print(f"{formatted_key:<18}: {formatted_value}")
    
    print("="*50)

def gerar_graficos(dados: list):
    """
    Gera e exibe múltiplos gráficos para análise dos dados.
    
    Parâmetros:
        dados (list): Lista de valores numéricos
    """
    if not dados:
        print("\nNenhum dado para visualizar!")
        return
    
    fig, axs = plt.subplots(1, 3, figsize=(18, 5))
    fig.suptitle('Análise Visual dos Dados', fontsize=16)
    
    # Gráfico de linha
    axs[0].plot(dados, 'o-', color='royalblue')
    axs[0].set_title('Série Temporal dos Valores')
    axs[0].set_xlabel('Posição na Sequência')
    axs[0].set_ylabel('Valor')
    axs[0].grid(True, linestyle='--', alpha=0.7)
    
    # Histograma
    sns.histplot(dados, kde=True, color='crimson', ax=axs[1])
    axs[1].set_title('Distribuição de Frequências')
    axs[1].set_xlabel('Valor')
    axs[1].set_ylabel('Frequência')
    
    # Boxplot
    sns.boxplot(y=dados, color='limegreen', ax=axs[2])
    axs[2].set_title('Diagrama de Caixa (Boxplot)')
    axs[2].set_ylabel('Valores')
    
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()
    
    salvar = input("\nDeseja salvar os gráficos? (s/n): ").lower()
    if salvar == 's':
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"analise_grafica_{timestamp}.png"
        fig.savefig(filename, dpi=300, bbox_inches='tight')
        print(f"Gráficos salvos como '{filename}'")

def exportar_dados(dados: list):
    """
    Exporta os dados coletados para um arquivo CSV.
    
    Parâmetros:
        dados (list): Lista de valores numéricos
    """
    if not dados:
        print("\nNenhum dado para exportar!")
        return
    
    df = pd.DataFrame(dados, columns=['Valores'])
    estatisticas = calcular_estatisticas(dados)
    
    # Adiciona estatísticas como novas linhas
    for key, value in estatisticas.items():
        df = df.append({'Valores': f"{key}: {value:.4f}"}, ignore_index=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"dados_exportados_{timestamp}.csv"
    
    df.to_csv(filename, index=False)
    print(f"\nDados exportados para '{filename}'")
    print(f"Total de valores: {len(dados)}")
    print("Estatísticas incluídas no arquivo")

def main():
    """Função principal que orquestra o fluxo do programa."""
    print("\n" + "="*50)
    print("ANALISADOR ESTATÍSTICO COM VISUALIZAÇÃO GRÁFICA".center(50))
    print("="*50)
    print("Este programa permite:")
    print("- Coletar números via entrada interativa")
    print("- Calcular diversas estatísticas descritivas")
    print("- Visualizar os dados através de múltiplos gráficos")
    print("- Exportar resultados para arquivos\n")
    
    dados = coletar_numeros()
    
    if dados:
        estatisticas = calcular_estatisticas(dados)
        exibir_estatisticas(estatisticas)
        
        if len(dados) > 1:
            plot = input("\nDeseja visualizar os gráficos? (s/n): ").lower()
            if plot == 's':
                gerar_graficos(dados)
        
        export = input("\nDeseja exportar os dados? (s/n): ").lower()
        if export == 's':
            exportar_dados(dados)
    
    print("\n" + "="*50)
    print("Processo concluído!".center(50))
    print("="*50)

if __name__ == "__main__":
    main()