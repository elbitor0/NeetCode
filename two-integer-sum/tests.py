from solution import Solution

tests = [
    ([2, 7, 11, 15], 9, [0, 1]),          # classique
    ([3, 2, 4], 6, [1, 2]),               # paire au milieu
    ([3, 3], 6, [0, 1]),                   # deux mêmes nombres
    ([1, 2, 3, 4, 5], 9, [3, 4]),          # somme à la fin
    ([5, 75, 25], 100, [1, 2]),            # somme au milieu
    ([0, 4, 3, 0], 0, [0, 3]),             # zéros
    ([-1, -2, -3, -4, -5], -8, [2, 4]),    # négatifs
    ([1, 2, 3, 4, 5, 6], 7, [0, 5]),       # extrémités
    ([1, 3, 5, 7], 10, [2, 3]),            # fin de tableau
    ([2, 5, 9, 11], 14, [1, 3]),           # milieu + fin
    ([1, 2, 3, 4, 4], 8, [3, 4]),          # doublons en fin
    ([1, 2, 3, 4, 5], 3, [0, 1]),          # petite somme
    ([10, 20, 10, 40, 50, 60, 70], 50, [2, 3]), # paire non initiale
    ([1, 5, 1, 5], 10, [1, 3]),            # plusieurs doublons
    ([0, 1, 2, 3, 4], 5, [1, 4])           # somme au milieu/fond
]

sol = Solution()

for nums, target, expected in tests:
    result = sol.twoSum(nums, target)
    assert result == expected, f"Failed for nums={nums}, target={target}, got {result}"
    print(f"OK: nums={nums}, target={target} -> {result}")

print("Tous les tests passent ✅")
