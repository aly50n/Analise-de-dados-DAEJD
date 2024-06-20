import pandas as pd
from scipy.stats import ttest_rel, f_oneway

# Dados de frequência cardíaca pré-jogo e pós-jogo para cada jogo
data_pre_jogo_inside = {
    'ID_Jogador': ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                   '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'],
    'ps': [129, 116, 111, 105, 110, 101, 106, 112, 132, 114, 130, 126, 123, 119, 131, 103, 129, 157, 166, 106]
}

data_pos_jogo_inside = {
    'ID_Jogador': ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                   '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'],
    'ps': [126, 125, 105, 114, 106, 92, 94, 114, 130, 117, 116, 121, 113, 128, 140, 128, 127, 139, 115, 112]
}

data_pre_jogo_phasmophobia = {
    'ID_Jogador': ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                   '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'],
    'ps': [132, 125, 120, 98, 111, 107, 88, 107, 130, 110, 116, 121, 113, 128, 140, 128, 127, 139, 115, 112]
}

data_pos_jogo_phasmophobia = {
    'ID_Jogador': ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'],
    'ps': [136, 133, 123, 113, 114, 92, 102, 127, 148, 115, 129, 130, 113, 130, 130, 116, 124, 130, 150, 106]
}

data_pre_jogo_rocketleague = {
    'ID_Jogador': ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'],
    'ps': [126, 120, 116, 97, 109, 95, 113, 117, 126, 120, 131, 127, 117, 135, 122, 129, 95, 141, 159, 111]
}

data_pos_jogo_rocketleague = {
    'ID_Jogador': ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'],
    'ps': [112, 116, 113, 121, 111, 101, 113, 131, 132, 111, 130, 126, 123, 119, 131, 103, 129, 157, 166, 106]
}

data_pre_jogo_valorant = {
    'ID_Jogador': ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'],
    'ps': [131, 117, 116, 105, 123, 117, 112, 121, 142, 127, 124, 140, 116, 131, 137, 143, 130, 148, 143, 124]
}

data_pos_jogo_valorant = {
    'ID_Jogador': ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'],
    'ps': [134, 120, 125, 109, 99, 95, 112, 126, 141, 112, 131, 127, 117, 135, 122, 129, 95, 141, 156, 111]
}

# Convertendo os dicionários em DataFrames do pandas
df_pre_jogo_inside = pd.DataFrame(data_pre_jogo_inside)
df_pos_jogo_inside = pd.DataFrame(data_pos_jogo_inside)
df_pre_jogo_phasmophobia = pd.DataFrame(data_pre_jogo_phasmophobia)
df_pos_jogo_phasmophobia = pd.DataFrame(data_pos_jogo_phasmophobia)
df_pre_jogo_rocketleague = pd.DataFrame(data_pre_jogo_rocketleague)
df_pos_jogo_rocketleague = pd.DataFrame(data_pos_jogo_rocketleague)
df_pre_jogo_valorant = pd.DataFrame(data_pre_jogo_valorant)
df_pos_jogo_valorant = pd.DataFrame(data_pos_jogo_valorant)

# Calculando média e desvio padrão do pré/pós jogo para cada frequência
def calcular_stats(dataframe):
    stats_df = dataframe.describe().loc[['mean', 'std']].transpose()
    return stats_df

# Calculando estatísticas descritivas para pré/pós jogo
stats_pre_jogo_inside = calcular_stats(df_pre_jogo_inside)
stats_pos_jogo_inside = calcular_stats(df_pos_jogo_inside)
stats_pre_jogo_phasmophobia = calcular_stats(df_pre_jogo_phasmophobia)
stats_pos_jogo_phasmophobia = calcular_stats(df_pos_jogo_phasmophobia)
stats_pre_jogo_rocketleague = calcular_stats(df_pre_jogo_rocketleague)
stats_pos_jogo_rocketleague = calcular_stats(df_pos_jogo_rocketleague)
stats_pre_jogo_valorant = calcular_stats(df_pre_jogo_valorant)
stats_pos_jogo_valorant = calcular_stats(df_pos_jogo_valorant)

# Exibindo as estatísticas descritivas
print("Estatísticas descritivas para Pré-Inside:")
print(stats_pre_jogo_inside)
print("Estatísticas descritivas para Pós-Inside:")
print(stats_pos_jogo_inside)

print("Estatísticas descritivas para Pré-Phasmophobia:")
print(stats_pre_jogo_phasmophobia)
print("Estatísticas descritivas para Pós-Phasmophobia:")
print(stats_pos_jogo_phasmophobia)

print("Estatísticas descritivas para Pré-Rocket League:")
print(stats_pre_jogo_rocketleague)
print("Estatísticas descritivas para Pós-Rocket League:")
print(stats_pos_jogo_rocketleague)

print("Estatísticas descritivas para Pré-Valorant:")
print(stats_pre_jogo_valorant)
print("Estatísticas descritivas para Pós-Valorant:")
print(stats_pos_jogo_valorant)

# Função para calcular o teste t pareado
def calcular_teste_t_pareado(df_pre, df_pos):
    resultados_t_pareado = {}
    for coluna in df_pre.columns[1:]:  # Começa da segunda coluna para evitar 'ID_Jogador'
        t_statistic, p_valor = ttest_rel(df_pre[coluna], df_pos[coluna])
        resultados_t_pareado[coluna] = {'t_statistic': t_statistic, 'p_valor': p_valor}
    return pd.DataFrame(resultados_t_pareado).transpose()

# Calculando teste t pareado para cada jogo
resultado_t_inside = calcular_teste_t_pareado(df_pre_jogo_inside, df_pos_jogo_inside)
resultado_t_phasmophobia = calcular_teste_t_pareado(df_pre_jogo_phasmophobia, df_pos_jogo_phasmophobia)
resultado_t_rocketleague = calcular_teste_t_pareado(df_pre_jogo_rocketleague, df_pos_jogo_rocketleague)
resultado_t_valorant = calcular_teste_t_pareado(df_pre_jogo_valorant, df_pos_jogo_valorant)

print("Resultado do teste t pareado para Inside:")
print(resultado_t_inside)
print("\n")

print("Resultado do teste t pareado para Phasmophobia:")
print(resultado_t_phasmophobia)
print("\n")

print("Resultado do teste t pareado para Rocket League:")
print(resultado_t_rocketleague)
print("\n")

print("Resultado do teste t pareado para Valorant:")
print(resultado_t_valorant)
print("\n")