aluguel_carro = int(input("Quantos dias você alugou o carro? "))
km_rodados = float(input("Quantos km você rodou com o carro? "))

valor_total = (aluguel_carro * 60) + (km_rodados * 0.15)

print('O valor total a ser pago é: R${:.2f}'.format(valor_total))