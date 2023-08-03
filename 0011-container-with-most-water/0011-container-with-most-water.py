class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_amount = 0
        i = 0
        j = len(height) - 1
        while i < j:
            max_amount = max(max_amount, (j-i)*min(height[i], height[j]))
            if height[i] < height[j]:
                i+=1
            else:
                j-=1
        
        return max_amount