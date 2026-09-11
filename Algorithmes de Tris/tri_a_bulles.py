# algos tri à bulles
def tri_bulles_iteratif(T: list):
    n = len(T)
    permut = True

    while permut:
        permut = False
        for i in range(n-1):
            if T[i] > T[i+1]:
                permut = True
                tmp = T[i]
                T[i] = T[i+1]
                T[i+1] = tmp
        n -= 1

def tri_bulles_recursif(T: list):
    n = len(T)
    permut = False

    for i in range(n - 1):
        if T[i] > T[i + 1]:
            permut = True
            tmp = T[i]
            T[i] = T[i + 1]
            T[i + 1] = tmp

    if permut:
        permut = False
        return tri_bulles_recursif(T[:n-1]) + [T[n-1]]
    else:
        return T


T1 = [2,9,20,6,10,2,0,15,6,8,1,5,3,2,7]
T2 = [2,9,20,6,10,2,0,15,6,8,1,5,3,2,7]

tri_bulles_iteratif(T1)
T = tri_bulles_recursif(T2)

print(f"T1 trié = {T1}")
print(f"T2 trié = {T}")