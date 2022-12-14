# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Rmj-5goRcql-vZTLveKn8-X6UHuN0w62
"""

# Importando Bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

# Upload do arquivo
from google.colab import files
arq = files.upload()

# Criando DataFrame
df = pd.read_excel("AdventureWorks.xlsx")

# Visualizado as 5 primeiras linhas
df.head()

# Quantidade de linhas e colunas
df.shape

# Verificando os tipos de dados
df.dtypes

# Receita total
df['Valor Venda'].sum()

# Custo Total
df['Custo'] = df['Custo Unitário'].mul(df['Quantidade'])#Criando coluna de custo

df.head(1)



# Custo Total
round(df['Custo'].sum(), 2)# Round para arredondar as casas decimais

# Criar coluna de Lucro
df['Lucro'] = df['Valor Venda'] - df['Custo']
df.head(1)

#Total Lucro
round(df['Lucro'].sum(),2)

# Coluna com Total de Dias para Envio do Produto
df['Tempo_evio'] = df['Data Envio'] - df['Data Venda']
df.head(1)

# Extraindo apenas dias
df['Tempo_envio'] = (df['Data Envio'] - df['Data Venda']).dt.days
df.head(1)

# Verificando o Tipo da Coluna Tempo_envio
df['Tempo_envio'].dtype

# Média do Tempo de Envio por Marca
df.groupby('Marca')['Tempo_envio'].mean()

# Verifivando Valores Faltantes
df.isnull().sum()

# Agrupar por Ano e Marca
df.groupby([df['Data Venda'].dt.year, 'Marca'])['Lucro'].sum()

pd.options.display.float_format = '{:20,.2f}'.format

# Restando o Index
Lucro_ano = df.groupby([df['Data Venda'].dt.year, 'Marca'])["Lucro"].sum().reset_index()
Lucro_ano

# Total de Produtos Vendidos
df.groupby('Produto')['Quantidade'].sum().sort_values(ascending=False)

# Gráfico Total Produtos Vendidos
df.groupby('Produto')['Quantidade'].sum().sort_values(ascending=True).plot.barh(title='Total Produtos Vendidos')
plt.xlabel('Total')
plt.ylabel('Produto')

df.groupby(df['Data Venda'].dt.year)['Lucro'].sum().plot.bar(title='Lucro x Ano')
plt.xlabel('Ano')
plt.ylabel('Receita')

df.groupby(df['Data Venda'].dt.year)['Lucro'].sum()

# Vendas de 2009
df_2009 = df[df['Data Venda'].dt.year == 2009]
df_2009.head()

df_2009.groupby(df_2009['Data Venda'].dt.month)['Lucro'].sum().plot(title='Lucro x Mês')
plt.xlabel('Mês')
plt.ylabel('Lucro')

from matplotlib.image import pil_to_array
df_2009.groupby('Marca')['Lucro'].sum().plot.bar(title='Lucro x Marca')
plt.xlabel('Marca')
plt.ylabel('Lucro')
plt.xticks(rotation='horizontal')

df_2009.groupby('Classe')['Lucro'].sum().plot.bar(title='Lucro x Classe')
plt.xlabel('Classe')
plt.ylabel('Lucro')
plt.xticks(rotation='horizontal')

df['Tempo_envio'].describe()

# Gráfico de Boxplot
plt.boxplot(df['tempo_envio'])

# Histograma
plt.hist(df['Tempo_envio'])

#Tempo Mínimo de Envio
df['tempo_envio'].min()

#Tempo Máximo de Envio
df['tempo_envio'].max()

#Outlier
df[df['Tempo_Envio'] == 20]

df.to_csv('df_Análise_de_dados_Pandas.csv', index=False)

