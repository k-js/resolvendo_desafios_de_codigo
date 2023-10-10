valor = float(input())

if valor > 0:
  print("Deposito realizado com sucesso!\nSaldo atual: R$ {:.2f}".format(valor))
elif valor == 0:
  print(f"Encerrando o programa...")
else:
  print(f"Valor invalido! Digite um valor maior que zero.")