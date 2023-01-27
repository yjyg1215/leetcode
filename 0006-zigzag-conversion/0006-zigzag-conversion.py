class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1:
            return s
        
        zig=[[] for _ in range(numRows)]
        row=0
        flag=0 #0: 아래 방향, 1: 위 방향
        for i in range(len(s)):
            if row>(numRows-1):
                flag=1
                row-=2
            elif row<0:
                flag=0
                row+=2
            
            if flag==0:
                zig[row].append(s[i])
                row+=1
            else:
                zig[row].append(s[i])
                row-=1
        
        res=""
        for i in list(map(''.join,zig)):
            res+=i
            
        return res
            
            