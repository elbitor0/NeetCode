from solution import Solution

tests = [
    ([1, 2, 4, 6], [48, 24, 12, 8]),
    ([-1, 0, 1, 2, 3], [0, -6, 0, 0, 0]),
    ([1, 0, 3, 0], [0, 0, 0, 0]),
    ([2, 3, 4, 5], [60, 40, 30, 24]),
    ([-1, -2, -3, -4], [-24, -12, -8, -6]),
    ([-1, 2, -3, 4], [-24, 12, -8, 6]),
    ([5, 7], [7, 5]),
    ([1, 1, 1, 1], [1, 1, 1, 1]),
    ([-1, -1, -1, -1], [-1, -1, -1, -1]),
    ([20, -20, 1, -1], [20, -20, 400, -400]),
    ([0, 4, 5], [20, 0, 0]),
    ([4, 5, 0], [0, 0, 20])
]

sol = Solution()

for i, (nums, expected) in enumerate(tests, 1):
    assert sol.productExceptSelf(nums) == expected, f"Test {i} failed"

print("✅ All tests passed")
