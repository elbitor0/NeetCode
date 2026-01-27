import pytest
from solution import Solution
# 🔁 utilitaire pour comparer sans dépendre de l'ordre
def normalize(result):
    return sorted([sorted(group) for group in result])

sol = Solution()
def test_basic_example():
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    expected = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    assert normalize(sol.groupAnagrams(strs)) == normalize(expected)
#test_basic_example()
print(ord('a'))
def test_single_word():
    assert normalize(sol.groupAnagrams(["abc"])) == [["abc"]]


def test_empty_list():
    assert normalize(sol.groupAnagrams([])) == []


def test_two_anagrams():
    assert normalize(sol.groupAnagrams(["ab", "ba"])) == [["ab", "ba"]]


def test_no_anagrams():
    strs = ["ab", "cd", "ef"]
    expected = [["ab"], ["cd"], ["ef"]]
    assert normalize(sol.groupAnagrams(strs)) == normalize(expected)


def test_duplicate_words():
    strs = ["abc", "abc", "abc"]
    expected = [["abc", "abc", "abc"]]
    assert normalize(sol.groupAnagrams(strs)) == normalize(expected)


def test_repeated_letters():
    strs = ["aab", "aba", "baa", "abb"]
    expected = [["aab", "aba", "baa"], ["abb"]]
    assert normalize(sol.groupAnagrams(strs)) == normalize(expected)


def test_different_frequencies():
    strs = ["aabb", "bbaa", "abab", "abbb"]
    expected = [["aabb", "bbaa", "abab"], ["abbb"]]
    assert normalize(sol.groupAnagrams(strs)) == normalize(expected)


def test_case_sensitivity():
    strs = ["eat", "Tea", "ate"]
    expected = [["eat", "ate"], ["Tea"]]
    assert normalize(sol.groupAnagrams(strs)) == normalize(expected)


def test_empty_strings():
    strs = ["", "", "a"]
    expected = [["", ""], ["a"]]
    assert normalize(sol.groupAnagrams(strs)) == normalize(expected)


def test_spaces():
    strs = ["a b", "b a", "ab"]
    expected = [["a b", "b a"], ["ab"]]
    assert normalize(sol.groupAnagrams(strs)) == normalize(expected)

def test_long_strings():
    strs = ["a" * 1000, "a" * 1000, "a" * 999 + "b"]
    expected = [["a" * 1000, "a" * 1000], ["a" * 999 + "b"]]
    assert normalize(sol.groupAnagrams(strs)) == normalize(expected)


def test_many_small_words():
    strs = ["a", "b", "a", "b", "c"]
    expected = [["a", "a"], ["b", "b"], ["c"]]
    assert normalize(sol.groupAnagrams(strs)) == normalize(expected)


def test_bad_key_trap():
    strs = ["ab", "ba", "abc", "cab"]
    expected = [["ab", "ba"], ["abc", "cab"]]
    assert normalize(sol.groupAnagrams(strs)) == normalize(expected)


def test_all_anagrams():
    strs = ["bca", "abc", "cba"]
    expected = [["bca", "abc", "cba"]]
    assert normalize(sol.groupAnagrams(strs)) == normalize(expected)
