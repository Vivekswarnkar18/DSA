class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n=len(nums)
        mp={}
        for i in range(n):
            val=target-nums[i]
            if val in mp:
                return [mp[val],i]
            mp[nums[i]]=i
        return []
        