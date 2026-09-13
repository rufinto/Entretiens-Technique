def tri_fusion(T: list):
    n = len(T)

    if n > 1:
        m = n // 2
        g = T[:m]
        d = T[m:]

        tri_fusion(g)
        tri_fusion(d)

        i, j, k = 0, 0, 0

        while i < len(g) and j < len(d):
            if g[i] < d[j]:
                T[k] = g[i]
                i += 1
            else:
                T[k] = d[j]
                j += 1
            k += 1

        while i < len(g):
            T[k] = g[i]
            i += 1
            k += 1
        while j < len(d):
            T[k] = d[j]
            j += 1
            k += 1

T = [2,9,20,6,10,2,0,15,6,8,1,5,3,2,7]

tri_fusion(T)

print(f"T trié = {T}")