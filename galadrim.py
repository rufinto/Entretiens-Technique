"""

On te donne un tableau d'entiers `nums` et un entier `k`.

Trouve la sous-array contiguë de longueur **exactement** `k` qui a la **moyenne maximale**, et retourne cette moyenne.

### Exemple

`Input:  nums = [1, 12, -5, -6, 50, 3], k = 4`

`Output: 12.75`

**Explication :** La sous-array `[12, -5, -6, 50]` a une somme de 51, soit une moyenne de 51/4 = **12.75**.

### Contraintes

`1 <= k <= nums.length <= 10^5`

`-10^4 <= nums[i] <= 10^4`

"""

"""
[1, 12, -5, -6, 50, 3], k = 4`

1, 12, -5, -6, => 2:4

"""
def sous_array_optimal(nums, k):

    element_0 = nums[0]
    som = sum(nums[:k])
    moyenne = som/k # O(k)

    for i in range(k, len(nums)): # O(n-k)
        tmp_som = som - element_0 + nums[i] # O(k)
        tmp_moyenne = tmp_som/k
        if tmp_moyenne > moyenne:
            moyenne = tmp_moyenne
            som = tmp_som
            element_0 = nums[i-k+1]

    return moyenne

print(sous_array_optimal([-1, -12, -5, -6, -50, -3], 4))


