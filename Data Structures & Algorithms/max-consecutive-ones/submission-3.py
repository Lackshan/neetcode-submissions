class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxConsecutiveOnes = 0

        tempConsecutiveOnes = 0
        for num in nums:
            if num == 1:
                tempConsecutiveOnes = tempConsecutiveOnes + 1
            else: # num is 0
                # Save on a write operation if they're equal
                if tempConsecutiveOnes > maxConsecutiveOnes:
                    maxConsecutiveOnes = tempConsecutiveOnes
                
                # Now we zero out the temp variable
                tempConsecutiveOnes = 0
        
        # We need another one of these checks in case
        # the final number is one.
        if tempConsecutiveOnes > maxConsecutiveOnes:
            maxConsecutiveOnes = tempConsecutiveOnes

        return maxConsecutiveOnes