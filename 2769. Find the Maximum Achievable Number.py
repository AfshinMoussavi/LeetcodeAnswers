#  Name   :   Find the Maximum Achievable Number
#  URL    :   https://leetcode.com/problems/find-the-maximum-achievable-number/description/
#  Github :   https://github.com/AfshinMoussavi

class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return sum(num,2*t)
