class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # We use Kadane's algorithm
        # We only care about the sum so no need
        # for the sliding window variation

        maxSum = nums[0]
        currSum = 0

        for n in nums:
            currSum = max(currSum, 0)
            currSum += n
            maxSum = max(maxSum, currSum)
        
        return maxSum