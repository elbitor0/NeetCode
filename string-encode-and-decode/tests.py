from solution import Solution

tests = [
    [],
    ["hello"],
    ["", "", ""],
    ["", "abc", "", "def"],
    ["hello world", " data ", " "],
    ["a#b#c", "12@34!", "$%^&*"],
    ["###", "##", "#"],
    ["123", "456789", "0"],
    ["a" * 1000, "b" * 500],
    ["", "#", "123#456", " ", "long string with spaces and # and 123"],
    ["a", "ab", "abc", "a"]
]
sol = Solution()
for i, strs in enumerate(tests, 1):
    enc = sol.encode(strs)
    dec = sol.decode(enc)
    print(f'strs = {strs}')
    print(f'enc = {enc}')
    print(f'dec = {dec}')
    assert dec == strs, f"Test {i} failed"

print("✅ All tests passed")
