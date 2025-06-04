import pandas as pd

# prompt: importrquivo xlsx

import pandas as pd
df = pd.read_excel('/content/arquivodeteste.xlsx')ar a

# prompt: visualizar dataframe

df = pd.read_excel('/content/arquivodeteste.xlsx')
print(df)

print(df.columns.tolist())

# prompt: remover coluna TRAVEL

df = df.drop(columns=['TICKET'])
df

# prompt: Corrigir valores de Travel, colocando como nomes próprios, só a primeira letra maiúscula

df['TRAVEL'] = df['TRAVEL'].str.capitalize()
df