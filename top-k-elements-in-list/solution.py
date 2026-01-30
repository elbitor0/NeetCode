from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        histo = {}
        res = []
        for n in nums:
            if n in histo:
                histo[n]+=1
            else:
                histo[n] = 1
        
        bucket = [[] for _ in range(len(nums))]
        for (key,val) in histo.items():
            bucket[val-1].append(key)
        i = len(nums)-1
        while len(res) < k:
            res+=bucket[i]
            i-=1
        return res
            