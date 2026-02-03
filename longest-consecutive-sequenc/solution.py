from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_dict = dict.fromkeys(nums,1)
        for n in nums:
            if n-1 not in nums_dict and nums_dict[n] == 1:
                m = n+1
                while m in nums_dict:
                    nums_dict[n]+=1
                    m+=1
            
        res = 0
        for v in nums_dict.values():
            if v > res:
                res = v
        return res

sol = Solution()
l = [0,3,7,2,5,8,4,6,0,1]
print(sol.longestConsecutive(l))