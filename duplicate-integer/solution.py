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

    def fusion2(self, l1: List[int], l2: List[int]):
        len1 = len(l1)
        len2 = len(l2)
        i=j=0
        while j<len2:
            if i == len1 or l2[j] <= l1[i]:
                l1.insert(i,l2[j])
                j+=1
                len1+=1
            i+=1
        return l1

    def fusion_sort(self,nums: List[int]) -> List[int]:
        length = len(nums)
        if length <= 2:
            if length ==2 and nums[1]<nums[0]:
                nums = [nums[1],nums[0]]
            return nums
        else:
            l1 = self.fusion_sort(nums[:(length//2)])
            l2 = self.fusion_sort(nums[(length//2):])
        return self.fusion2(l1,l2)

    def hasDuplicate(self, nums: List[int]) -> bool:
        nums = self.fusion_sort(nums)
        for i in range(1,len(nums)):
            if nums[i-1] == nums[i]:
                return True
        return False