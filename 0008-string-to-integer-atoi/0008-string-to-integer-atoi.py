class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """          
        res=0
        i=0
        sign=1
        while i<len(s) and s[i]==' ':
            i+=1
        
        if i<len(s) and s[i]=='-':
            sign=-1
            i+=1
        elif i<len(s) and s[i]=='+':
            i+=1
            
        while i<len(s) and s[i].isdigit():
            res=res*10+int(s[i])
            i+=1
        
        res*=sign
        if res>2**31-1:
            return 2**31-1
        elif res<-(2**31):
            return -(2**31)
        else:
            return res