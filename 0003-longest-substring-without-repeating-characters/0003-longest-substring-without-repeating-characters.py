class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 1
        try:
            tmp_str = s[0]
        except:
            return 0
        
        for i in range(1,len(s)):
            if s[i] not in tmp_str:
                tmp_str+=s[i]
            else:
                if max_len<len(tmp_str):
                    max_len=len(tmp_str)
                tmp_str=tmp_str.split(s[i])[1]
                tmp_str+=s[i]
        
        if len(tmp_str)>max_len:
            max_len=len(tmp_str)
        
        return max_len
                    
                
            