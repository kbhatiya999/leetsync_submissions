class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        from collections import Counter
        c = Counter(nums)
        for count in c.values():
            if count > 1:
                return True
        return False