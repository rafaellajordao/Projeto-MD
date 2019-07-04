def solução(a, b, c): #def para a solução da equação.
    i = 0
    while i * a <= c: #valor de a deve ser menor que c, pois ax + by = c.
        if (c - (i * a)) % b == 0: #o resto deve ser zero, pois devemos gastar o saldo inteiro.
            print("c) X = ", i ,", Y = ",
            int((c - (i * a)) / b)) #print da solução da equação, com os valores de X e Y.
            return 0
        i = i + 1


def letra_a(a, b, c): #def para informar se a equação tem solução, ou não.
    i = 0
    while i * a <= c:
        if (c - (i * a)) % b == 0:
            print("a) Tem solução") #resposta da letra a, informando se a equação tem solução.
            return 0
        i = i + 1

    print("a) Sem solução") #resposta da lera a informando que a equação não tem solução.
while True:
    a = int(input("Insira valor para A: ")) #input para o valor do primeiro produto.
    b = int(input("Insira valor para B: ")) #input para o valor do segundo produto.
    c = int(input("Insira valor para C: ")) #input para o valor do saldo total.
    letra_a(a, b, c) #def para a letra a
    solução(a, b, c) #def para a letra c

