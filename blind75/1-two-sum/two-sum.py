class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a hashmap for storing number and it's index
        # anyone looking for complement can check it in here
        # if complement found they will get complemen's index too

        hashmap = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return hashmap[complement], i # keeping ascending order of index
            hashmap[num] = i
