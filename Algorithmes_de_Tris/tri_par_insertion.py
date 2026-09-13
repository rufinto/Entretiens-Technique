def tri_par_insertion(T: list):

    for i in range(1, len(T)):
        tmp = T[i]
        j = i - 1

        while j >= 0 and T[j] > tmp:
            T[j+1] = T[j]
            j -= 1
            T[j+1] = tmp


T = [2,9,20,6,10,2,0,15,6,8,1,5,3,2,7]

tri_par_insertion(T)

print(f"T trié = {T}")