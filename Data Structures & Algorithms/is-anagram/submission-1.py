class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        for l_s in s:
            idx = t.find(l_s)
            if idx == -1:
                return False
            else:
                t = t[:idx] + t[idx+1:]

        return True

        