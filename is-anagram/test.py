from solution import Solution
import time

tests = [
    ("listen", "silent", True),            # anagramme simple
    ("triangle", "integral", True),        # anagramme
    ("apple", "pale", False),              # pas anagramme, longueurs différentes
    ("night", "thing", True),              # anagramme
    ("dusty", "study", True),              # anagramme
    ("schoolmaster", "theclassroom", True),# anagramme avec plusieurs lettres
    ("conversation", "voicesranton", True),# anagramme
    ("xx", "bb", False),                  # petit exemple
    ("aabbcc", "abcabc", True),            # lettres répétées
    ("aabbcc", "aabbc", False),            # longueur différente
    ("listen", "silents", False),          # un caractère en plus
    ("Hello", "hello", False),             # sensibilité à la casse
    ("funeral", "real fun", False),        # espace inclus, pas anagramme
    ("", "", True),                         # deux chaînes vides
    ("a", "a", True)                        # une seule lettre
]

sol = Solution()
a1 = time.time()
for s, t, expected in tests:
    result = sol.isAnagram(s, t)
    assert result == expected, f"Anagram: Test failed for ({s}, {t}). Got {result}, expected {expected}"
    print(f"OK: ({s}, {t}) -> {result}")
b1 = time.time()
print(b1-a1)

a2 = time.time()
for s, t, expected in tests:
    result = sol.isAnagram2(s, t)
    assert result == expected, f"Anagram2: Test failed for ({s}, {t}). Got {result}, expected {expected}"
    print(f"OK: ({s}, {t}) -> {result}")
b2 = time.time()
print(b2-a2)

print("Tous les tests passent ✅")
