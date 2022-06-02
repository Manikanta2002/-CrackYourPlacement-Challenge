#SortColours
#https://leetcode.com/problems/sort-colors/
class Solution(object):
    def sortColors(self, nums):
        for i in range(len(nums)):
            for j in range(i):
                if nums[j]>nums[i]:
                    temp=nums[j]
                    nums[j]=nums[i]
                    nums[i]=temp

