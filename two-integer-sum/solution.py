from typing import List

class Solution:
    def fusion(self,l1: List[int], l2: List[int]):
        len1 = len(l1)
        len2 = len(l2)
        i=j=0
        result = []

        while i <len1 and j<len2:
            if l1[i] < l2[j]:
                result.append(l1[i])
                i+=1
            else:
                result.append(l2[j])
                j+=1
        while i<len1:
            result.append(l1[i])
            i+=1
        while j<len2:
            result.append(l2[j])
            j+=1
        
        return result
    
    def fusion_sort(self,nums: List[int]) -> List[int]:
        length = len(nums)
        if length <= 2:
            if length ==2 and nums[1]<nums[0]:
                nums = [nums[1],nums[0]]
            return nums
        else:
            l1 = self.fusion_sort(nums[:(length//2)])
            l2 = self.fusion_sort(nums[(length//2):])
        return self.fusion(l1,l2)

    def rec_twoSum(self, sorted_nums: List[int], target:int, i:int, j:int):
        if i<0 or j >= len(sorted_nums):
            return []
        shot = sorted_nums[i] + sorted_nums[j]
        if  shot == target:
            return [i,j]
        elif shot<target:
            try1 = self.rec_twoSum(sorted_nums,target, i,j+1)
            if len(try1) == 0:
                try2 = self.rec_twoSum(sorted_nums,target, i+1,j)
            else:
                try2 = []
        else:
            try1 = self.rec_twoSum(sorted_nums,target, i-1,j)
            if len(try1) == 0:
                try2 = self.rec_twoSum(sorted_nums,target, i,j-1)
            else:
                try2 = []
        return try1 + try2

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = self.fusion_sort(nums)
        length = len(sorted_nums)
        i=(length//2)-1
        j=i+1

        (i,j) = self.rec_twoSum(sorted_nums, target, i,j)
        num1 = sorted_nums[i]
        num2 = sorted_nums[j]
        res = []
        k=0
        for loop in range(2):
            while nums[k] != num1 and nums[k]!= num2:
                k+=1
            res.append(k)
            k+=1
        
        return res