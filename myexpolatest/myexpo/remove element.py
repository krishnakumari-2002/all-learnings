class Solution(object):
    def removeElement(self, nums, val):
        k=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[k]=nums[i]
                k+=1
        return k       

obj=Solution()
nums= [0,1,2,2,3,0,4,2]
val = 2
objects=obj.removeElement(nums,val)
print("object",objects)
print("Filtered array:", nums[:objects])