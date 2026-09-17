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
            
    # def get_most_frequent_char(freq: map) -> tuple[str, int]:
    #     ch = 0
    #     f = freq[ch]

    #     for i in range(1, 26):
    #         if freq[i] > f:
    #             f = freq[i]
    #             ch = i
        
    #     return chr(ch + ord("a")), f