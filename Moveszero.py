class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        k=0
        for num in nums:
            if(num!=0):
                nums[k]=num
                k+=1
        for x in range(k,len(nums)):
            nums[x]=0
