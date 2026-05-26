class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(a for a in s if a.isalnum())
        cleaned = cleaned.lower()

        i = 0
        j = len(cleaned) - 1

        # works only for odds
        while i < j:
            if cleaned[i] != cleaned[j]:
                return False
            i += 1
            j -= 1


        return True