class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        mp={}
        for num in nums:
            if num in mp:
                mp[num]+=1
            else:
                mp[num]=1
        arr=sorted(mp,key=mp.get,reverse=True)
        return arr[:k]
        
        
       