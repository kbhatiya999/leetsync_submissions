class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        win_chars = set()
        left = ans = 0
        
        # window [left, right] i.e inclusive
        for right in range(len(s)):
            
            while s[right] in win_chars:
                win_chars.remove(s[left])
                left += 1

                
            win_chars.add(s[right])
            ans = max(ans, right - left + 1) # current window size
        
        return ans

