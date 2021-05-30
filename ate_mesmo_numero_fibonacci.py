a = 1
b = 1
c = 0
resul = 0
#i = 0
while True:
    if b >= (4000000):
        break
    if b % 2 == 0:
        resul += b
    c = a
    a = b
    b = a + c       
print(f'Soma dos termos de valor par que não excedem 4 milhões: {resul} Alerei')
