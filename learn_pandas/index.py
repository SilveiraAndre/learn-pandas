# importacao da biblioteca pandas | importing the pandas library
import pandas as pd
# importacao da biblioteca pandas | importing the pandas library
import numpy as np

# leitura do arquivo CSV com delimitador ponto e virgula | reading the CSV file with semicolon delimiter
df = pd.read_csv('data\\origin\\dados.csv', sep=';')

# exibicao das colunas do DataFrame | displaying the columns of the DataFrame
print(df.columns)

# exibicao das primeiras linhas do DataFrame | displaying the first rows of the DataFrame
print(df.head())

# exibicao das ultimas linhas do DataFrame | displaying the last rows of the Dataframe
print(df.tail())

# SERIES - exibicao de uma coluna especifica do DataFrame | displaying a specific column of the DataFrame
print(type(df['data_venda']))

# DATAFRAME - exibicao de colunas especificas do DataFrame | displaying specific columns of the DataFrame
print(type(df[['produto','vendedor']]))

# exibicao de colunas especificas do DataFrame atraves de uma lista | displaying specific columns of the DataFrame through a list
colunas = ['data_venda', 'vendedor']
print(df[colunas])

# exibicao de uma linha especifica do DataFrame atraves do locator | displaying a specific row of the DataFrame through the locator
print(df.loc[0, ['produto','vendedor']])

# exibicao de linhas e colunas especificas do DataFrame atraves do ilocator | displaying specific rows and columns of the DataFrame through the ilocator
print(df.iloc[0:6, 0:3])

# exibicao dos indices do DataFrame | displaying the indices of the DataFrame
print(df.index)

# alteracao do indice do DataFrame para a coluna 'data_venda', uso de inplace=True para modificar o DataFrame original | changing the index of the DataFrame to the 'data_venda' column, using inplace=True to modify the original DataFrame
df.set_index('data_venda', inplace=True)
print(df)

# exibicao do shape (dimensoes) do DataFrame | displaying the shape (dimensions) of the DataFrame
print(df.shape)

# exibicao das informacoes do DataFrame | displaying the information of the DataFrame
print(df.info())
 
# exibicao das estatisticas descritivas do DataFrame | displaying the descriptive statistics of the DataFrame
df['valor_total'] = df['valor_unitario'] * df['quantidade']
print(df.head())

# adicionando uma nova coluna ao DataFrame com valores NaN | adding a new column to the DataFrame with NaN values
df['campo_1'] = np.nan
print(df.head())
print(df.info())

# removendo a coluna 'campo_2' do DataFrame | removing the 'campo_2' column from the DataFrame
df['campo_2'] = 'deletar registros'
print(df.head())
df.drop(columns=['campo_2'], inplace=True)
print(df.head())

# exibicao da contagem de valores unicos na coluna 'produto' | displaying the count of unique values in the 'produto' column
print(df['produto'].value_counts())

# exibicao dos valores unicos na coluna 'vendedor' | displaying the unique values in the 'vendedor' column
print(df['vendedor'].unique())

# exibicao da quantidade de valores unicos na coluna 'vendedor' | displaying the count of unique values in the 'vendedor' column
print(df['vendedor'].nunique())

# agrupamento dos dados por vendedor e soma dos valores totais, ordenando de forma decrescente | grouping the data by seller and summing the total values, sorting in descending order
print(df.groupby('vendedor')['valor_total'].sum().sort_values(ascending=False))

# criando uma tabela pivot com soma dos valores totais por produto e vendedor | creating a pivot table with the sum of total values by product and seller
print(df.pivot_table(
    index='produto',
    values='valor_total',
    aggfunc='sum',
    columns='vendedor',
    fill_value=0,
    margins=True
)
)

# filtrando o DataFrame para exibir apenas as linhas onde o produto é 'Colchão' | filtering the DataFrame to display only the rows where the product is 'Colchão'
print(df.query('produto == "Colchão"'))

# convertendo o index para data para usar filtro com loc | converting the index to date to use filter with loc
df.index = pd.to_datetime(df.index)
print(df.loc["2020"])

# removendo coluna campo_1 para exportar arquivo | removing campo_1 column to export file
df.drop(columns=['campo_1'], inplace=True)

# exportando o DataFrame modificado para um novo arquivo CSV | exporting the modified DataFrame to a new CSV file
df.to_csv('data\\to_export\\dados_modificado.csv', sep=';', index=True)
print("Arquivo exportado com sucesso!")
