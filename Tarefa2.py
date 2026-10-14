# Criar um datafame a partir do funcionário.csv
#Criar uma coluna chamada "Salario_maior_5000" que terá os valores "possui" e "não possui" crie ela a partir da coluna "salario"
#renomear a coluna "ativo" para "emepregado"

import pandas as pd 

df = pd.read_csv(r"C:\Users\rayssa.christina\Downloads\funcionarios.csv")

df = df[df['ativo'] == True]

df["Salario_maior_5000"] = df["salario"].apply(lambda x: "possui" if x > 5000 else "não possui")

df = df.rename(columns={"ativo": "empregado"})

print(df)
