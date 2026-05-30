class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Since this is a duplicate finding problem
        # we want to use hashsets

        # We'd only use hashmaps if we cared about the
        # number of times a char appears

        length = -1 # Problem defines len(s) as >= 0
        window = set()
        L = 0

        for R in range(len(s)):
            while s[R] in window:
                window.remove(s[L])
                L += 1
            window.add(s[R])
            length = max(R-L+1, length)
        return 0 if length == -1 else length

    