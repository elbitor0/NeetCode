from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = []
        i = 0
        while i<len(nums) and len(zeros) < 2:
            if nums[i] == 0:
                zeros.append(i)
            i+=1
        if len(zeros) == 2:
            return []*len(nums)
        elif len(zeros) == 1:
            res = [0]*len(nums)
            for e in nums[0:nums[zeros[0]]]:
                res[zeros[0]] *=e
            for e in nums[nums[zeros[0]]:]:
                res[zeros[0]] *=e
        else:
            res= [1]*len(nums)
            for e in nums[1:]:
                res[0]*=e
            for i in range(1,len(nums)):
                res[i] *=res[i-1]//nums[i]*nums[i-1]
                
        return res
sol = Solution()
l = [-1, 0, 1, 2, 3]
print(sol.productExceptSelf(l))