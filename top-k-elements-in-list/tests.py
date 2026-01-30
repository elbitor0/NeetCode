from solution import Solution

sol = Solution()
tests = [
    # Example de l'énoncé
    {
        "nums": [1, 2, 2, 3, 3, 3],
        "k": 2,
        "output": [2, 3]
    },

    # Un seul élément
    {
        "nums": [1],
        "k": 1,
        "output": [1]
    },

    # Nombres négatifs
    {
        "nums": [-1, -1, -2, -2, -2, -3],
        "k": 2,
        "output": [-2, -1]
    },

    # k = nombre d’éléments distincts
    {
        "nums": [4, 4, 5, 6],
        "k": 3,
        "output": [4, 5, 6]
    },

    # Fréquences bien distinctes
    {
        "nums": [7, 7, 7, 8, 8, 9],
        "k": 1,
        "output": [7]
    }
]

for t in tests:
    result = sol.topKFrequent(t["nums"], t["k"])
    assert set(result) == set(t["output"]), f"Failed for {t}"