vendas = [1000, 1500, 1200, 1300]
vendedores = ["Mariana", "Sofia", "Daniel", "Pedro"]

qnt_vendas = len(vendas)
qnt_vendedores = len(vendedores)
soma = sum(vendas)

for i, venda in enumerate(vendas):
    media = vendas[i] / soma
    print(f'{vendedores[i]} vendeu {vendas[i]} e sua media foi de {media:.0%}')

