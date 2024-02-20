class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        
        result = 0
        pre = s[-1]
        for i in s[::-1]:
            if roman[i] < roman[pre]:
                result -= roman[i]
            else:
                result += roman[i]
            pre = i
        
        return result
            