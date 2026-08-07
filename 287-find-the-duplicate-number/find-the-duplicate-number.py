class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mp={}
        for num in nums:
            if num in mp:
                return num
            else:
                mp[num]=1
        
        