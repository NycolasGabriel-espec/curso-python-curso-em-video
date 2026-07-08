largura_parede = float(input("Digite a largura da parede: "))
altura_parede = float(input("Digite a altura da parede: "))

area_parede = largura_parede * altura_parede

tinta_necessaria = area_parede / 2

print('A área da parede é de {:.2f} m² e a quantidade de tinta necessária para pintar a parede é de {:.2f} litros'.format(area_parede, tinta_necessaria))