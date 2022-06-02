#https://leetcode.com/problems/remove-duplicates-from-sorted-array/
#Remove Duplicates from Sorted Array
class Solution(object):
    def removeDuplicates(self, nums):
        i=0
        for j in range(1,len(nums)):
            if nums[i]==nums[j]:
                continue
                
            else:
                nums[i+1]=nums[j]
                i=i+1
        
        return i+1