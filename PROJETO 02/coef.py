def comb(n, k):
    if k == 0 or k == n: #CONDIÇÃO PARA IMPRIMIR O VALOR DA COMBINAÇÃO QUANDO K FOR IGUAL A ZERO OU K E N TENHAM O MESMO VALOR
        return 1
    elif n < k:
        print("Inválido. Lembre-se que n precisa ser maior que k.") #PRINT PARA IMPRIMIR UMA MENSAGEM CASO OS VALORES DOS INPUTS SEJAM INVÁLIDOS
    else:
        return comb(n-1, k-1) + comb(n-1, k) #FÓRMULA PARA CALCULAR O VALOR DA COMBINAÇÃO, CASO EXISTA

n = int(input("Insira o valor de n: ")) #INPUT QUE PEDE O VALOR DE N PARA QUE SEJA POSSÍVEL CALCULAR A COMBINAÇÃO
k = int(input("Insira o valor de k: ")) #INPUT QUE PEDE O VALOR DE K

print("C{},{} = {}".format(n, k, comb(n, k))) #PRINT PARA IMPRIMIR O VALOR DA COMBINAÇÃO