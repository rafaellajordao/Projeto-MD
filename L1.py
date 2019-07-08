# L1 :::::::::::::::::::::::::::::::::::::
def lógica(): #DEF PARA O MENU DO PROGRAMA

    print("="*80)
    print("")
    p = int(input("""Valor lógico do primeiro termo:
    0 - falso   1 - verdadeiro
        """))
    print("")
    q = int(input("""Valor lógico do primeiro termo:
    0 - falso   1 - verdadeiro
        """))
    print("")
    print("="*80)
    res = int(input("""
1 - Conjução
2 - Disjunção
3 - Disjunção Exclusiva
4 - Condicional
5 - Bicondicional
Escolha uma operação lógica:"""))
    print("")
    print("="*80)

    if res == 1: #CONDIÇÃO PARA CONJUNÇÕES
        if p == 1 and q == 1:
            print("Verdadeiro!")
        if p == 1 and q == 0:
            print("Falso!")
        if p == 0 and q == 1:
            print("Falso!")
        if p == 0 and q == 0:
            print("Falso!")

    if res == 2: #CONDIÇÃO PARA DISJUNÇÕES
        if p == 1 and q == 1:
            print("Verdadeiro!")
        if p == 1 and q == 0:
            print("Verdadeiro!")
        if p == 0 and q == 1:
            print("Verdadeiro!")
        if p == 0 and q == 0:
            print("Falso!")

    if res == 3: #CONDIÇÕES PARA OU EXCLUSIVO
        if p == 1 and q == 1:
            print("Falso!")
        if p == 1 and q == 0:
            print("Verdadeiro!")
        if p == 0 and q == 1:
            print("Verdadeiro!")
        if p == 0 and q == 0:
            print("Falso!")

    if res == 4: #CONDIÇÕES PARA CONDICIONAIS (HAHA)
        if p == 1 and q == 1:
            print("Verdadeiro!")
        if p == 1 and q == 0:
            print("Falso!")
        if p == 0 and q == 1:
            print("Verdadeiro!")
        if p == 0 and q == 0:
            print("Verdadeiro!")

    if res == 5: #CONDIÇÕES PARA BICONDICIONAIS
        if p == 1 and q == 1:
            print("Verdadeiro!")
        if p == 1 and q == 0:
            print("Falso!")
        if p == 0 and q == 1:
            print("Falso!")
        if p == 0 and q == 0:
            print("Verdadeiro!")
    pass

lógica() #EXECUTAR A DEF
