# Lista com os valores de faturamento diário
faturamento = [
    31490.7866, 37277.9400, 37708.4303, 0.0000, 0.0000, 17934.2269, 0.0000, 
    6965.1262, 24390.9374, 14279.6481, 0.0000, 0.0000, 39807.6622, 27261.6304, 
    39775.6434, 29797.6232, 17216.5017, 0.0000, 0.0000, 12974.2000, 28490.9861, 
    8748.0937, 8889.0023, 17767.5583, 0.0000, 0.0000, 3071.3283, 48275.2994, 
    10299.6761, 39874.1073
]

# Filtrar os dias com faturamento acima de zero
faturamento_valido = [valor for valor in faturamento if valor > 0]

# Menor valor de faturamento ocorrido em um dia do mês
menor_valor = min(faturamento_valido)

# Maior valor de faturamento ocorrido em um dia do mês
maior_valor = max(faturamento_valido)

# Calcular a média mensal considerando apenas os dias com faturamento válido
media_mensal = sum(faturamento_valido) / len(faturamento_valido)

# Número de dias em que o faturamento foi superior à média mensal
dias_acima_da_media = len([valor for valor in faturamento_valido if valor > media_mensal])

# Exibir os resultados
print("Menor valor de faturamento ocorrido em um dia do mês:", menor_valor)
print("Maior valor de faturamento ocorrido em um dia do mês:", maior_valor)
print("Número de dias com faturamento superior à média mensal:", dias_acima_da_media)

