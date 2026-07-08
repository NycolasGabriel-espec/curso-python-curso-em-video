preco_produto = float(input("Digite o preço do produto: "))

desconto = preco_produto * 0.05

preco_final = preco_produto - desconto

print('O preço do produto com desconto de 5% é de R$ {:.2f}'.format(preco_final))