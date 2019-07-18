graph = {'a':{'b':1,'c':2, 'd':3},
        'b':{'d':2, 'e':4},
        'c':{'d':5, 'f':3},
        'd':{'e':2, 'f':1, 'g':4}, 
        'e':{'g':2, 'h':5},
        'f':{'g':1, 'i':3},
        'g':{'j':5, 'h':3, 'i':4},
        'h':{'j':2},
        'i':{'j':1}, 
        'j':{}}
n1 = (input("Início: ")).lower()
n2 = (input("Fim: ")).lower()
def djikstra(graph, start, end):
    ant = {}
    dist_min = {}
    unseenNo = graph
    caminho = []
    inf = 999999
    for no in unseenNo:
        dist_min[no] = inf
    dist_min[start] = 0

    while unseenNo:
        minNo = None
        for no in unseenNo:
            if minNo is None:
                minNo = no
            elif dist_min[no] < dist_min[minNo]:
                minNo = no

        for childNo, valor in graph[minNo].items():
            if valor + dist_min[minNo] < dist_min[childNo]:
                dist_min[childNo] = valor + dist_min[minNo]
                ant[childNo] = minNo
        unseenNo.pop(minNo)

    currentNo = end
    while currentNo != start:
        try:
            caminho.insert(0, currentNo)
            currentNo = ant[currentNo]
        except KeyError:
            print("IMPOSSIVEL.")
            break
    caminho.insert(0, start)
    if dist_min[end] != inf:
        print("Menor caminho: " + str(dist_min[end]))
        print("Caminho: " + str(caminho))

djikstra(graph, n1, n2)
