from typing import List


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

    def isAnagram2(self, s: str, t: str) -> bool:
        length = len(t)
        if length != len(s):
            return False
        sorted_s = self.fusion_sort(list(s))
        sorted_t = self.fusion_sort(list(t))
        for i in range(length):
            if sorted_s[i] != sorted_t[i]:
                return False
        return True