class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """        
        if x<0:
            flag=-1
            x*=-1
        else:
            flag=1
        
        res=int(str(x)[::-1])*flag
        
        if (res<-2**31) or res>(2**31-1):
            return 0
        else:
            return res