class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = defaultdict(int)
        dup = 0
        longest = 0

        left, right = 0, 0
        while right < len(s):
            ch_right = s[right]
            freq[ch_right] += 1

            if freq[ch_right] == 2:
                dup += 1
            
            right += 1

            while dup > 0:
                ch_left = s[left]
                freq[ch_left] -= 1

                if freq[ch_left] == 1:
                    dup -= 1
                
                left += 1
            
            longest = max(longest, right - left)

        return longest