class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        result = ""
        
        if num >= 1000:
            result += 'M'*(num//1000)
            num %= 1000
        if num >= 500:
            if num >= 900:
                result += 'CM'
                num -= 900
            else:
                result += 'D'
                num -= 500
        if num >= 100:
            if num >= 400:
                result += 'CD'
                num -= 400
            else:
                result += 'C'*(num//100)
                num %= 100
        if num >= 50:
            if num >= 90:
                result += 'XC'
                num -= 90
            else:
                result += 'L'
                num -= 50
        if num >= 10:
            if num >= 40:
                result += 'XL'
                num -= 40
            else:
                result += 'X'*(num//10)
                num %= 10
        if num >= 5:
            if num >= 9:
                result += 'IX'
                num -= 9
            else:
                result += 'V'
                num -= 5
        if num >= 1:
            if num == 4:
                result += 'IV'
            else:
                result += 'I'*num
        
        return result