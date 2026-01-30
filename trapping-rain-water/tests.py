from solution import Solution

tests = [
    # Exemple de l’énoncé
    {
        "height": [0,2,0,3,1,0,1,3,2,1],
        "output": 9
    },

    # Cas minimal
    {
        "height": [0],
        "output": 0
    },

    # Deux barres seulement
    {
        "height": [2, 1],
        "output": 0
    },

    # Tout plat
    {
        "height": [0, 0, 0, 0],
        "output": 0
    },

    # Strictement croissant
    {
        "height": [0, 1, 2, 3, 4],
        "output": 0
    },

    # Strictement décroissant
    {
        "height": [4, 3, 2, 1, 0],
        "output": 0
    },

    # Un seul bassin simple
    {
        "height": [3, 0, 3],
        "output": 3
    },

    # Plusieurs bassins
    {
        "height": [3, 0, 1, 3, 0, 5],
        "output": 8
    },

    # Plateau au sommet
    {
        "height": [2, 2, 0, 2, 2],
        "output": 2
    },

    # Pics irréguliers
    {
        "height": [4, 2, 0, 3, 2, 5],
        "output": 9
    },

    # Grande vallée
    {
        "height": [5, 0, 0, 0, 5],
        "output": 15
    },

    # Alternance
    {
        "height": [1,0,1,0,1,0,1],
        "output": 3
    }
]

sol = Solution()

for t in tests:
    result = sol.trap(t["height"])
    print(result)
    assert result == t["output"], f"Failed for {t}"