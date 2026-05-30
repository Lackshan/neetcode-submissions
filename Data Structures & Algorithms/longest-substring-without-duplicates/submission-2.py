class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Since this is a duplicate finding problem
        # we want to use hashsets

        # We'd only use hashmaps if we cared about the
        # number of times a char appears

        length = 0
        window = set()
        L = 0

        for R in range(len(s)):
            while s[R] in window:
                window.remove(s[L])
                L += 1
            window.add(s[R])
            length = max(R-L+1, length)
        return length

# Time Complexity = O(n)
# Space Complexity = Since we are using a hash set, extra space
# is bounded by the max size of the hashmap, so it's O(26) because
# of the english alphanet, this simplifies to O(1)
    