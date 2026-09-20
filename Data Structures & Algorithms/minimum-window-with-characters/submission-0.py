class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = defaultdict(int)
        have = defaultdict(int)

        for ch in t:
            need[ch] += 1

        left, right = 0, 0
        include = 0
        res = (0, float('inf'))

        while right < len(s):
            s_right = s[right]
            have[s_right] += 1
            right += 1

            if s_right in need and have[s_right] == need[s_right]:
                include += 1

            while left < right and include >= len(need):
                s_left = s[left]
                
                if s_left in need and have[s_left] == need[s_left]:
                    include -= 1

                have[s_left] -= 1

                if right - left < res[1] - res[0]:
                    res = (left, right)
                
                left += 1

        return "" if res[1] == float('inf') else s[res[0]:res[1]]

