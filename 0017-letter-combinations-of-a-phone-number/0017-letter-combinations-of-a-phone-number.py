class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return ""
        
        mapping = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        result = []
        def recur(mapping, pre, digits, result):
            letters = mapping[digits[0]]
            for letter in letters:
                if len(digits) > 1:
                    recur(mapping, pre+letter, digits[1:], result)
                else:
                    result.append(pre+letter)
        
        recur(mapping, "", digits, result)
        
        return result
        