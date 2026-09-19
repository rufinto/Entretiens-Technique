# write an algorithm which compute all the subsets of a set

"""
ex: set = {a,b,c}
nbr of subset 2^3 = 8
{}, {a}, {b}, {c}, {a, b}, {a, c}, {c, b}, {a, b, c}

"""

def subset_of_a_set(set, memo = []):
    if len(set) == 0:
        return []
    if len(set) == 1:
        return [[], set]

    memo.append([])
    memo.append(set)

    for i in range(len(set)):
        j = i
        reached = []
        while j < len(memo[set]):
            reached.append(set[i])
            j += 1
    