def recaman(n):
    if (n <= 0):
        return

    print(0, ",", end='')
    L = set([])
    L.add(0)

    RAFA = 0
    for i in range(1, n):

        VIVI = RAFA / i

        if (VIVI < 0 or VIVI in L):
            VIVI = RAFA * i

        L.add(VIVI)

        print(VIVI, ",", end='')
        RAFA = VIVI

if __name__ == '__main__':
    n = int(input("Número de elementos: "))
    recaman(n)