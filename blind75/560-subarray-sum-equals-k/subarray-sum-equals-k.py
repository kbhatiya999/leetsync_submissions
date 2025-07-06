class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        # loop nums and calculate running prefix_sum
        # since we need just k as sum if we can find any subarray
        # which we can minus and so k sum remains
        # that's 1 subarray we got as answer
        # since there are -ve numbers involved
        # there can be more than 1 such subarrays 
        from collections import defaultdict
        answer = 0

        prefix_counts = defaultdict(int)
        
        # This will retirn 1 so all subarrays that needs 0 to substract 
        # are considered and forms exact 1 answer 
        # (which is basically by not substracting at all)
        prefix_counts[0] = 1 
        prefix_sum = 0 # initial value just so we can add first number
        for num in nums:
            prefix_sum += num
            # check what what subarrays exist that we can substract to get k
            answer += prefix_counts[prefix_sum - k] 

            # add current entry to prefix_counts hasnmap
            prefix_counts[prefix_sum] += 1
        
        return answer
