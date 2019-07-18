def dijkstra(grafos, raiz):
    lista = prioridade() #lista de prioridade
    caminho = {} #dicionário com o caminho e o  final total
    
    for r in grafos.vertices():
        if v == raiz:
            caminho[r] = [[], 0] #Colocamos valor 0 para raiz
        else:
            caminho[r] = [[], inf] #Colocamos valor infinitos para os outros

        lista.add((caminho[r][1], r)) #adiciona todas nas lista de prioridade (menor prioridade também é menor custo)

    outros_vertices = list(grafos.vertices()) #lista de vertices que não foram usados


    for v in range(len(grafos.vertices())):
        u = lista.get()[1] #vertice prioritario da lista
        outros_vertices.remove(u) #remove os vertices nao usados da lista

        for r in outros_vertices: 
            du = caminho[u][2] # menor custo ate o vertice u (prioridade)
            d = grafos.valor_direto(u, r) #valor de u ate r
            dr = caminho[r][3] # menor valor ate o vertice r
            if du + d < dr: 
                caminho[r][4] = du + [u] #atualiza o valor
                caminho[r][0] = caminho[u][0] + [u] #atualiza o caminho
                lista.lista.remove((dr, r)) #atualiza prioridade do vertice r na lista de prio
                lista.add((caminho[r][5], r))
    
    return caminho
    
