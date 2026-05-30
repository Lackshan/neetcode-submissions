class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = len(nums) + 1
        L, currSum = 0, 0

        for R in range(len(nums)):
            currSum += nums[R]
            while currSum >= target:
                # Advance L
                length = min(R - L + 1, length)
                currSum -= nums[L]
                L += 1
        return 0 if length == len(nums) + 1 else length
        