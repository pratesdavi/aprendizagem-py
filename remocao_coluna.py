"""
Script para Manipulação de Dados com Pandas

OBJETIVO:
  - Demonstrar a criação e manipulação básica de um DataFrame
  - Ilustrar a remoção segura de colunas
  - Fornecer exemplo didático para projetos de análise de dados

Data: 02.05.2025
Versão: 1.0
"""

import pandas as pd

# =============================================================================
# 1. CRIAÇÃO DO DATAFRAME DE EXEMPLO
# =============================================================================
"""
Estrutura dos dados:
  - name: Nome do passageiro (string)
  - price: Valor do ticket (numérico)
  - travel: Destino (string)
  - ticket: Código do bilhete (string)
"""
dados_exemplo = {
    'name': ['João', 'Maria', 'Pedro'],
    'price': [100, 150, 200],
    'travel': ['RJ', 'SP', 'MG'],  # Corrigido 'trevel' para 'travel'
    'ticket': ['A123', 'B456', 'C789']
}

# Criar DataFrame a partir do dicionário
df = pd.DataFrame(dados_exemplo)

print("DataFrame Original:")
print(df)
print("\n" + "-"*50 + "\n")  # Separador visual

# =============================================================================
# 2. REMOÇÃO DE COLUNA
# =============================================================================
"""
Motivação:
  - A coluna 'price' não é necessária para esta análise
  - Boa prática: Criar novo DataFrame ao invés de sobrescrever o original
    (preserva dados brutos para auditoria)
"""
df_processado = df.drop(columns=['price'])

# =============================================================================
# 3. RESULTADO FINAL
# =============================================================================
print("DataFrame Após Processamento:")
print(df_processado)

# =============================================================================
# 4. INFORMAÇÕES ADICIONAIS (para contexto)
# =============================================================================
"""
Etapas Comuns em Fluxos de Dados:
  1. Extração: Carregar dados de fonte externa
  2. Transformação: (exemplo: remoção de colunas)
  3. Carregamento: Salvar resultado (não implementado aqui)
"""
