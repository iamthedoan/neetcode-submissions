class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_chars = {}
        l_count = 0
        l_window = 0

        for i in range(len(s)):
            if s[i] in seen_chars.keys() and seen_chars[s[i]] >= l_window:
                l_window = seen_chars[s[i]] + 1

            seen_chars[s[i]] = i
            window = i + 1 - l_window
            if window > l_count:
                l_count = window

        return l_count