class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        str_x=str(x)
        rev_x=str_x[::-1]
        
        return str_x==rev_x