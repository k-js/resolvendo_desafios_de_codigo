valor_inicial = float(input())
taxa_juros = float(input())
periodo = int(input())

def calcular_valor_final(valor_inicial, taxa_juros, periodo):
    valor_final = round((valor_inicial * (1 + taxa_juros)**periodo), 2)
    return valor_final

valor_final = calcular_valor_final(valor_inicial, taxa_juros, periodo)

print(f"Valor final do investimento: R$ {valor_final:.2f}")