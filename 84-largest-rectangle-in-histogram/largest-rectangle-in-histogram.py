class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        left=[0]*n
        right=[0]*n
        stack=[]
        for i in range(n-1,-1,-1):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            if not stack:
                right[i]=n
            else:
                right[i]=stack[-1]
            stack.append(i)
        stack.clear()
        for i in range(n):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            if not stack:
                left[i]=-1
            else:
                left[i]=stack[-1]
            stack.append(i)
        maxi=0
        for i in range(n):
            width=right[i]-left[i]-1
            area=heights[i]*width
            maxi=max(area,maxi)

        return maxi