class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        mp={}
        for i in range(n):
            val=target-nums[i]
            if val in mp:
                return [mp[val],i]
            mp[nums[i]]=i
        return []