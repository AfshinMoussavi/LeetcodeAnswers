#  Name   :   Contains Duplicate
#  URL    :   https://leetcode.com/problems/contains-duplicate/description/
#  Github :   https://github.com/AfshinMoussavi


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        db = set()
        for number in nums:
            if number in db:
                return True
            db.add(number)
        return False
