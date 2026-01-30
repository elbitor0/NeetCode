from typing import List
from numpy import array as arr

class Solution:  
    def str_value(self, str):
        res =[0]*26
        for c in str:
            res[ord(c) - 97] += 1
        return tuple(res)


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dico = {}
        for str in strs:
            str_val = self.str_value(str)
            if str_val in dico:
                dico[str_val].append(str)
            else:
                dico[str_val] = [str]
        res = list(dico.values())
        return res