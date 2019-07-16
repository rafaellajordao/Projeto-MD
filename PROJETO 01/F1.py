# F1 :::::::::::::::::::::::::::::::::::::::::::
cont = 0 #CONTADOR DE PARES
injetora = 0 #TIPO DE FUNÇÃO f(B) = f(A)
sobrejetora = 0 #TIPO DE FUNÇÃO x: A → B, ocorre a f(x) = B
dom = [] #CONJUNTO DOS DOMÍNIOS
im = [] #CONJUNTO DAS IMAGENS
numerador = 1 #NUMERADOR DE PARES
N = int(input("Quantidade de pares que serão adicionados: ")) #INPUT PARA A QUANTIDADE DE PARES
for i in range(N): #REPETIÇÃO
    D = input("""Valor do {}º domínio:  
    Se não houver, digite "nulo"
    ::: """.format(numerador)) # INPUT PARA VALORES DO DOMÍNIO COM O CONTADOR DE PARES
    I = input("""Valor da {}ª imagem:
    Se não houver, digite "nulo"
    ::: """.format(numerador)) #INPUT PARA VALORES DA IMAGEM COM O CONTADOR DE PARES
    dom.append(D) #ADICIONANDO VALORES DO DOMÍNIO À LISTA DOM
    im.append(I) #ADICIONANDO VALORES DA IMGAEM À LISTA IM
    numerador += 1 #NUMERADOR SOBE UM
    cont += 1 #CONTADOR SOBE UM

    if len(set(im)) == len(im): #FUNÇÃO LEN PARA CONTAR ELEMENTOS DA LISTA | SET PARA CHECAR SE HÁ VALORES REPETIDOS
        injetora += 1
    if im == "nulo":
        sobrejetora += 1

if sobrejetora != 0 and injetora != 0: #CONDIÇÃO PARA UMA FUNÇÃO INJETORA
    print("É uma função injetora.")
if sobrejetora == 0 and injetora == 0: #CONDIÇÃO PARA UMA FUNÇÃO SOBREJETORA
    print("É uma função sobrejetora.")
if sobrejetora == 0 and injetora != 0: #CONDIÇÃO PARA UMA FUNÇÃO BIJETORA
    print("A função é bijetora.")
