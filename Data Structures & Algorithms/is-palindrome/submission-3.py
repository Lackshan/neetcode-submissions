class Solution:
    def isPalindrome(self, s: str) -> bool:
        sanitisedString = ''.join(char for char in s if char.isalnum()).lower()

        L, R = 0, len(sanitisedString) - 1

        while L < R:
            if sanitisedString[L] != sanitisedString[R]:
                return False
            L += 1
            R -= 1
        return True
            
        