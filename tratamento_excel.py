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

# prompt: Preciso do segundo nome esteja em maiusculo. Se São paulo, colocar São Paulo.

def capitalize_second_name(name):
    parts = name.split()
    if len(parts) > 1:
        # Capitalize the second part, and keep the first part as is
        return f"{parts[0]} {' '.join(part.capitalize() for part in parts[1:])}"
    return name

df['TRAVEL'] = df['TRAVEL'].apply(capitalize_second_name)
df


# prompt: Coloco que o PRICE em REAL BR

import pandas as pd
df['PRICE'] = df['PRICE'].apply(lambda x: f"R$ {x:.2f}" if pd.notnull(x) else x)
df