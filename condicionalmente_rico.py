# Entrada de dados
saldo_total = int(input())
valor_saque = int(input())

if saldo_total >= valor_saque:
    saldo_atualizado = saldo_total - valor_saque
    mensagem = f"Saque realizado com sucesso. Novo saldo: {saldo_atualizado}"
else:
    mensagem = "Saldo insuficiente. Saque nao realizado!"

print(mensagem)