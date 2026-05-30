class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        runningSum = 0
        L, subArrCount = 0, 0

        for R in range(len(arr)):
            runningSum += arr[R]

            if R - L + 1 == k:
                windowAvg = runningSum / k
                if windowAvg >= threshold: subArrCount += 1

                runningSum -= arr[L]
                L += 1
        
        return subArrCount
            
