import pandas as pd
from scipy.stats import ttest_rel, f_oneway
from scipy.stats import shapiro
from scipy.stats import wilcoxon

def testar_normalidade(dataframe):
    """
    Testa a normalidade dos dados utilizando o teste de Shapiro-Wilk.

    Parametros:
    - dataframe: DataFrame contendo os dados a serem testados.

    Retorna:
    - Um dicionário onde as chaves são os nomes das colunas e os valores são mensagens indicando se os dados
      seguem uma distribuição normal ou não.
    """
    resultados_normalidade = {}
    alpha = 0.05  # Nível de significância
    
    for coluna in dataframe.columns[1:]:  # Ignorando a coluna 'ID_Jogador'
        stat, p_valor = shapiro(dataframe[coluna])
        if p_valor > alpha:
            resultados_normalidade[coluna] = 'Os dados parecem seguir uma distribuição normal (não rejeitamos H0)'
        else:
            resultados_normalidade[coluna] = 'Os dados não parecem seguir uma distribuição normal (rejeitamos H0)'
    
    return resultados_normalidade

# Dados pré-jogo fornecidos
data_pre_jogo = {
    'ID_Jogador': ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                   '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'],
    'Q1': [1, 1, 1, 1, 1, 1, 4, 1, 5, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1, 1],
    'Q2': [1, 1, 3, 1, 1, 5, 5, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 3, 1, 4],
    'Q3': [3, 1, 1, 3, 1, 1, 5, 3, 1, 1, 1, 3, 1, 1, 1, 1, 3, 1, 1, 3],
    'Q4': [3, 1, 3, 3, 1, 3, 5, 4, 3, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1],
    'Q5': [1, 1, 3, 3, 3, 1, 4, 3, 3, 1, 1, 4, 1, 1, 1, 3, 1, 1, 1, 3],
    'Q6': [1, 1, 4, 1, 1, 3, 4, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 3, 1, 1],
    'Q7': [1, 1, 3, 1, 1, 5, 4, 3, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1]
}


# Dados pós-jogo para os diferentes jogos
data_pos_valorant = {
    'ID_Jogador': ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                   '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'],
    'Q1': [3, 1, 3, 3, 1, 1, 1, 3, 1, 1, 3, 3, 1, 1, 1, 1, 3, 2, 1, 4],
    'Q2': [1, 1, 4, 2, 3, 3, 1, 1, 3, 1, 1, 2, 1, 1, 1, 1, 3, 1, 1, 3],
    'Q3': [1, 1, 1, 4, 3, 5, 1, 3, 3, 1, 1, 3, 1, 1, 1, 1, 2, 3, 1, 4],
    'Q4': [3, 1, 4, 5, 1, 4, 1, 4, 1, 1, 3, 3, 1, 1, 3, 3, 1, 1, 1, 5],
    'Q5': [1, 3, 3, 3, 2, 3, 1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 3, 2, 1, 4],
    'Q6': [3, 1, 3, 1, 5, 3, 1, 1, 1, 1, 1, 1, 1, 1, 3, 2, 1, 1, 1, 5],
    'Q7': [3, 1, 4, 1, 1, 5, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
}

data_pos_rocket_league = {
    'ID_Jogador': ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                   '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'],
    'Q1': [1, 1, 3, 3, 3, 5, 1, 1, 3, 1, 1, 4, 3, 3, 1, 3, 4, 4, 1, 1],
    'Q2': [1, 3, 5, 1, 1, 4, 3, 1, 1, 1, 3, 5, 1, 3, 1, 4, 4, 3, 1, 3],
    'Q3': [1, 1, 1, 4, 1, 4, 3, 3, 3, 1, 1, 4, 3, 4, 1, 3, 3, 4, 1, 1],
    'Q4': [3, 2, 4, 4, 2, 4, 4, 3, 4, 1, 1, 5, 3, 4, 2, 4, 4, 4, 1, 4],
    'Q5': [1, 1, 1, 3, 2, 4, 1, 1, 1, 1, 1, 5, 3, 4, 1, 4, 2, 1, 1, 4],
    'Q6': [3, 1, 5, 1, 3, 4, 1, 1, 1, 1, 1, 4, 1, 1, 3, 4, 4, 1, 1, 5],
    'Q7': [1, 1, 4, 1, 3, 4, 4, 1, 1, 1, 1, 4, 1, 1, 1, 3, 2, 1, 1, 1]
}

data_pos_inside = {
    'ID_Jogador': ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                   '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'],
    'Q1': [2, 3, 1, 4, 1, 1, 4, 3, 4, 1, 1, 3, 2, 1, 1, 1, 1, 3, 1, 4],
    'Q2': [3, 3, 1, 4, 4, 3, 1, 1, 3, 1, 1, 1, 2, 1, 1, 4, 4, 1, 1, 4],
    'Q3': [3, 2, 3, 4, 3, 3, 3, 3, 4, 1, 1, 1, 4, 3, 1, 4, 5, 1, 3, 5],
    'Q4': [4, 3, 1, 5, 4, 4, 4, 4, 5, 1, 1, 1, 4, 3, 2, 5, 4, 1, 1, 5],
    'Q5': [4, 3, 1, 4, 3, 3, 4, 3, 4, 1, 1, 1, 3, 1, 1, 4, 4, 1, 1, 5],
    'Q6': [3, 2, 3, 5, 3, 3, 4, 1, 4, 1, 3, 3, 2, 1, 3, 4, 2, 1, 1, 4],
    'Q7': [1, 1, 3, 3, 1, 3, 4, 1, 3, 1, 1, 1, 1, 1, 1, 1, 4, 1, 1, 1]
}

data_pos_phasmophobia = {
    'ID_Jogador': ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                   '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'],
    'Q1': [5, 3, 3, 5, 3, 5, 4, 5, 4, 4, 3, 5, 3, 4, 4, 3, 4, 3, 4, 5],
    'Q2': [5, 1, 1, 5, 4, 5, 1, 5, 4, 1, 3, 5, 1, 4, 4, 4, 4, 2, 1, 5],
    'Q3': [5, 3, 3, 5, 3, 5, 4, 5, 5, 1, 1, 5, 3, 4, 4, 4, 5, 4, 3, 5],
    'Q4': [5, 3, 1, 5, 3, 5, 4, 5, 4, 4, 3, 5, 5, 4, 2, 5, 4, 5, 1, 5],
    'Q5': [5, 2, 1, 5, 4, 5, 3, 5, 4, 1, 3, 5, 2, 1, 1, 4, 4, 5, 1, 5],
    'Q6': [5, 1, 3, 5, 4, 5, 1, 3, 4, 1, 1, 5, 1, 1, 3, 4, 2, 1, 1, 4],
    'Q7': [1, 1, 1, 5, 1, 5, 1, 5, 1, 4, 1, 5, 1, 4, 1, 4, 2, 1, 1, 5]
}

# Convertendo os dicionários em DataFrames do pandas
df_pre_jogo = pd.DataFrame(data_pre_jogo)
df_pos_valorant = pd.DataFrame(data_pos_valorant)
df_pos_rocket_league = pd.DataFrame(data_pos_rocket_league)
df_pos_inside = pd.DataFrame(data_pos_inside)
df_pos_phasmophobia = pd.DataFrame(data_pos_phasmophobia)

# Aplicando a função na base de dados pré-jogo
resultados_normalidade = testar_normalidade(df_pre_jogo)
resultados_normalidade_valorant = testar_normalidade(df_pos_valorant)
resultados_normalidade_rocket_league = testar_normalidade(df_pos_rocket_league)
resultados_normalidade_inside = testar_normalidade(df_pos_inside)
resultados_normalidade_phasmophobia= testar_normalidade(df_pos_phasmophobia)

# Exibindo os resultados
for coluna, resultado in resultados_normalidade.items():
    print(f'{coluna}: {resultado}')
    
for coluna, resultado in resultados_normalidade_valorant.items():
    print(f'{coluna}: {resultado}')

for coluna, resultado in resultados_normalidade_rocket_league.items():
    print(f'{coluna}: {resultado}')

for coluna, resultado in resultados_normalidade_inside.items():
    print(f'{coluna}: {resultado}')

for coluna, resultado in resultados_normalidade_phasmophobia.items():
    print(f'{coluna}: {resultado}')
    
# Calculando média e desvio padrão para cada jogo e cada pergunta
def calcular_stats(dataframe):
    stats_df = dataframe.describe().loc[['mean', 'std']].transpose()
    return stats_df

# Calculando estatísticas descritivas para cada jogo
stats_pre_jogo = calcular_stats(df_pre_jogo)
stats_valorant = calcular_stats(df_pos_valorant)
stats_rocket_league = calcular_stats(df_pos_rocket_league)
stats_inside = calcular_stats(df_pos_inside)
stats_phasmophobia = calcular_stats(df_pos_phasmophobia)

# Exibindo as estatísticas descritivas
print("Estatísticas descritivas para Pré-jogo:")
print(stats_pre_jogo)
print("Estatísticas descritivas para Valorant:")
print(stats_valorant)
print("\nEstatísticas descritivas para Rocket League:")
print(stats_rocket_league)
print("\nEstatísticas descritivas para Inside:")
print(stats_inside)
print("\nEstatísticas descritivas para Phasmophobia:")
print(stats_phasmophobia)


# Função para calcular o teste t pareado

def realizar_teste_wilcoxon(df_pre, df_pos):
    """
    Realiza o teste de Wilcoxon pareado para cada variável entre os DataFrames df_pre e df_pos.

    Parâmetros:
    - df_pre: DataFrame contendo os dados pré-jogo.
    - df_pos: DataFrame contendo os dados pós-jogo.

    Retorna:
    - Um DataFrame com os resultados do teste de Wilcoxon para cada variável.
    """
    resultados_wilcoxon = {}
    
    for coluna in df_pre.columns[1:]:  # Ignorando a coluna 'ID_Jogador'
        statistic, p_valor = wilcoxon(df_pre[coluna], df_pos[coluna])
        resultados_wilcoxon[coluna] = {'Estatística do teste': statistic, 'Valor p': p_valor}
    
    return pd.DataFrame(resultados_wilcoxon).transpose()
    
# Calculando teste t pareado para cada jogo
resultado_valorant = realizar_teste_wilcoxon(df_pre_jogo, df_pos_valorant)
resultado_rocket_league = realizar_teste_wilcoxon(df_pre_jogo, df_pos_rocket_league)
resultado_inside = realizar_teste_wilcoxon(df_pre_jogo, df_pos_inside)
resultado_phasmophobia = realizar_teste_wilcoxon(df_pre_jogo, df_pos_phasmophobia)

print("Resultado do teste wilcoxon para Valorant:")
print(resultado_valorant)
print("\nResultado do teste wilcoxon para Rocket League:")
print(resultado_rocket_league)
print("\nResultado do teste wilcoxon para Inside:")
print(resultado_inside)
print("\nResultado do teste wilcoxon para Phasmophobia:")
print(resultado_phasmophobia)
print("\n")