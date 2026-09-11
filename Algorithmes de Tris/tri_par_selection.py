def tri_selection_iteratif(T: list):
    n = len(T)

    for i in range(n):
        ind_min = i
        min = T[ind_min]

        for j in range(i+1, n):
            if T[j] < min:
                ind_min = j
                min = T[j]

        tmp = T[i]
        T[i] = min
        T[ind_min] = tmp

def tri_selection_recursif(T: list):
    n = len(T)
    if n == 1:
        return T
    elif n > 1:
        for i in range(n):
            ind_min = i
            min = T[ind_min]

            for j in range(i + 1, n):
                if T[j] < min:
                    ind_min = j
                    min = T[j]

            tmp = T[i]
            T[i] = min
            T[ind_min] = tmp

        return [T[0]] + tri_selection_recursif(T[1:])

T1 = [2,9,20,6,10,2,0,15,6,8,1,5,3,2,7]
T2 = [2,9,20,6,10,2,0,15,6,8,1,5,3,2,7]

tri_selection_iteratif(T1)
T = tri_selection_recursif(T2)

print(f"T1 trié = {T1}")
print(f"T2 trié = {T}")