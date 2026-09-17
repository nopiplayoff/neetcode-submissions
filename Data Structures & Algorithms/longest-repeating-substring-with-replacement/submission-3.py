class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        left, right = 0, 0
        longest = 0

        while right < len(s):
            s_right = s[right]
            
            freq[s_right] += 1
            right += 1
            
            while left < right and right - left - max(freq.values()) > k:
                s_left = s[left]
                freq[s_left] -= 1
                left += 1
            
            longest = max(longest, right - left)

        return longest