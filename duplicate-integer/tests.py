from solution import Solution
import time as ti

sol = Solution()

tests = [
    [],                             # liste vide
    [1],                            # un seul élément
    [2, 1],
    [1, 2],                         
    [5, 5, 5],                      
    [3, 1, 2],                      
    [8, 3, 4, 7, 10, 5, 2],         # cas general False
    [8, 3, 4, 7, 10, 5, 3],         # cas general True
    [-1, -3, -2, 0],                # nombres negatifs False
    [-1, -3, -3, 0],                # nombres negatifs True
    [1, 3, 2, 3, 1],                # opposes
    list(range(10, 0, -1))          # liste inversée
]

for t in tests:
    print(t, "->", sol.hasDuplicate(t))

#Two fusion time comparison

# Liste 1 : de 0 à 999, step 2 (1000 éléments au total)
list1 = list(range(0, 2000, 2))

# Liste 2 : de 1 à 1999, step 2 (1000 éléments au total)
list2 = list(range(1, 2000, 2))

t1f1 = ti.time()
sol.fusion(list1,list2)
t2f1 = ti.time()
print(t2f1-t1f1)

t1f2 = ti.time()
sol.fusion2(list1,list2)
t2f2 = ti.time()
print(t2f2-t1f2)