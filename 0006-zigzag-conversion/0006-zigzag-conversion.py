class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1:
            return s
        
        zig=[[0 for _ in range(len(s))] for _ in range(numRows)]
        row=0
        cul=0
        flag=0 #0: 아래 방향, 1: 위 방향
        for i in range(len(s)):
            if row>(numRows-1):
                flag=1
                row-=2
                cul+=1
            elif row<0:
                flag=0
                row+=2
                cul-=1
            
            if flag==0:
                zig[row][cul]=s[i]
                row+=1
            else:
                zig[row][cul]=s[i]
                row-=1
                cul+=1
        
        res=""
        for i in range(numRows):
            for j in range(len(s)):
                if zig[i][j]!=0:
                    res+=zig[i][j]
        
        return res
            
            