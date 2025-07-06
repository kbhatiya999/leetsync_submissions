class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # edge case k > n
        # Rotating complete array any no. of times makes no change to array
        # So only last rotation (incomplete rotation) matters
        n = len(nums)
        k = k % n
        # reverse last k elements - need reverse funtion
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        reverse(0, n-1)
        reverse(0,k-1)
        reverse(k, n-1)
