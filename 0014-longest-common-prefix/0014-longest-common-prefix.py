class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        cursor = 0
        while True:
            try:
                if len(set([x[cursor] for x in strs])) != 1:
                    break
                else:
                    prefix += strs[0][cursor]
                    cursor += 1
            except:
                break
        
        return prefix