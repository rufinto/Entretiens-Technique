def bfs(n,t,g):
    # ne peut pas être recursif

    if n == t:
        return True

    reached = {n: True}
    lnext = [n]

    while len(lnext) > 0:
        next = lnext.pop(0)

        for v in g[next]:

            if v == t:
                return True

            if v not in reached:
                reached[v] = True
                lnext.append(v)
    return False

g = [[2,4], [2,3,4], [0,1], [1,4,6,7], [0,1,3,5], [4,6,7], [3,5], [3,5]] # liste d'adjacence
n = 0
t = 7

print(bfs(n,t,g))