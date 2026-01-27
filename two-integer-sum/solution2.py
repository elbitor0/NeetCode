from typing import List
class Solution2:


    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dico = dict(zip(nums,[i for i in range(len(nums))]))
        for i in range(len(nums)):
            if target - nums[i] in dico and dico[target - nums[i]] != i:
                return [i, dico[target - nums[i]]] if i < dico[target - nums[i]] else dico[target - nums[i]]