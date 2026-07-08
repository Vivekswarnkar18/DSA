class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum=nums[0]
        currentSum=nums[0]
        n=len(nums)
        for i in range(1,n):
            currentSum=max(nums[i],currentSum+nums[i])
            maxSum=max(currentSum,maxSum)
        return maxSum
        