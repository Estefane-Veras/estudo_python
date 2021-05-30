maior = 0
for i in range(100, 1000, 1):
    for j in range(100, 1000, 1):
        produto = j*i
        temp = str(produto)
        inverso = temp[::-1]
        inverso = int(inverso)
        if inverso == produto and inverso > maior:
            maior = inverso

print(maior)
