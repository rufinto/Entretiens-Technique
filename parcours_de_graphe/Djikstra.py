def djikstra(n,t,g):

    reached = {n: True}
    frontiere = [n]
    parents = [0]*len(g)
    dist = [0]*len(g)

    while len(frontiere) > 0:
        id_min = 0
        min = dist[id_min]

        for val in range(1,len(frontiere)):
            if dist[val] < min:
                id_min = val
                min = dist[val]

        next = frontiere.pop(id_min)

        for v in g[next]:
            if v not in reached:
                reached[v] = True
                frontiere.append(v)
                parents[v] = next
                dist[v] = dist[next] + g[next][v]
            elif dist[v] > dist[next] + g[next][v]:
                dist[v] = dist[next] + g[next][v]

    chemin = [t]
    while chemin[0] != n:
        chemin = [parents[chemin[0]]] + chemin

    return chemin


# dictionnaire d'adjacence avec pondération
g = { 0: {2: 3, 4: 1},
      1: {2: 1, 3: 9, 4: 6},
      2: {0: 3, 1: 1},
      3: {1: 9, 4: 2, 6: 7, 7: 8},
      4: {0: 1, 1: 6, 3: 2, 5: 10},
      5: {4: 10, 6: 5, 7: 4},
      6: {3: 7, 5: 5},
      7: {3: 8, 5: 4}}
n = 0
t = 7

print(djikstra(n,t,g))