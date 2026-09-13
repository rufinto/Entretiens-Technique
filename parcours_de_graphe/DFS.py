def dfs_iteratif(n,t,g):

    if n == t:
        return True

    reached = {n: True}
    lnext = [n]

    while len(lnext) > 0:
        next = lnext.pop()
        for v in g[next]:
            if v == t:
                return True
            if v not in reached:
                reached[v] = True
                lnext.append(v)
    return False

def dfs_recursif(n,t,g):
    if n == t:
        return True

    for v in g[n]:
        if dfs_recursif(v,t,g):
            return True
    return False

g = [[2,4], [2,3,4], [0,1], [1,4,6,7], [0,1,3,5], [4,6,7], [3,5], [3,5]] # liste d'adjacence
n = 0
t = 7

print(dfs_iteratif(n,t,g))
#print(dfs_recursif(n,t,g))