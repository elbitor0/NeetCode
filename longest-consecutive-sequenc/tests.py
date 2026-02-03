from solution import Solution

tests = [
    # Exemples de l'énoncé
    ([2, 20, 4, 10, 3, 4, 5], 4),          # [2,3,4,5]
    ([0, 3, 2, 5, 4, 6, 1, 1], 7),         # [0,1,2,3,4,5,6]

    # Cas simples
    ([], 0),                              # tableau vide
    ([5], 1),                             # un seul élément
    ([1, 2, 3, 4, 5], 5),                 # déjà consécutif
    ([5, 4, 3, 2, 1], 5),                 # ordre inversé

    # Doublons
    ([1, 2, 2, 3], 3),                    # doublon au milieu
    ([1, 1, 1, 1], 1),                    # que des doublons

    # Séquences disjointes
    ([10, 5, 1, 3, 2, 20, 4], 5),          # [1,2,3,4,5]
    ([100, 4, 200, 1, 3, 2], 4),           # [1,2,3,4]

    # Nombres négatifs
    ([-1, -2, -3, -4], 4),                # [-4,-3,-2,-1]
    ([-2, -1, 1, 2, 3], 3),                # [1,2,3]
    ([-3, -2, -1, 0, 1], 5),               # [-3,-2,-1,0,1]

    # Cas limites
    ([10**9, -10**9], 1),                  # valeurs extrêmes
    ([7, 8, 9, 1, 2, 3], 3),               # deux suites max
]
sol = Solution()

for i, (nums, expected) in enumerate(tests, 1):
    result = sol.longestConsecutive(nums)
    print(f"Test {i}: {'OK' if result == expected else 'FAIL'}")
