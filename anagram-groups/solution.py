from typing import List
from numpy import array as arr

class Solution:  
    def isAnagram(self, s: str, t: str) -> bool:
        histogram = {}
        for c in s:
            histogram[c] = histogram.get(c,0)+1
        for c in t:
            histogram[c] = histogram.get(c,0)-1
        for v in histogram.values():
             if v != 0:
                return False
        return True

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dico = {}
        for str in strs:
            str_val = self.str_value(str)
            if str_val in dico:
                dico[str_val].append(str)
            else:
                dico[str_val] = [str]
        res = dico.values()
        return res