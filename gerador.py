import random

def gera_dezenas(qtd_sorteios, qtd_dezenas, nums_low, nums_high):
    dezenas = []
        
    for i in range(qtd_sorteios):
        sorteio = []
        for j in range(qtd_dezenas):
            sorteio.append(random.randint(nums_low[j], nums_high[j]))
        dezenas.append(sorted(sorteio))
    return dezenas

qtd_dezenas = 6
qtd_sorteios = 2

nums_low = [1, 5, 10, 20, 30, 40]
nums_high = [30, 40, 50, 60, 60, 60]
result = gera_dezenas(qtd_sorteios, qtd_dezenas, nums_low, nums_high)
print(result)