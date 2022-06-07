class Solution(object):
    def moveZeroes(self, nums):
        
        c=0
        l=len(nums)
        while c<l:
            if nums[c]==0:
                nums.append(nums.pop(c))
                c-=1
                l-=1
            c+=1