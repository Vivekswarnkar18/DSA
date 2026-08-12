class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n=len(height)
        i=0
        j=n-1
        maxi=0
        while i<j:
            w=j-i
            h=min(height[i],height[j])
            area=w*h
            maxi=max(maxi,area)
            if height[i]>height[j]:
                j-=1
            else:
                i+=1
        return maxi
        