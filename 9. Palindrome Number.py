#  Name   :   Palindrome Number
#  URL    :   https://leetcode.com/problems/palindrome-number/description/
#  Github :   https://github.com/AfshinMoussavi


class Solution:
    def isPalindrome(self, x: int) -> bool:
            s = str(x)
            if s == s[-1::-1]:
                return True
            return False
