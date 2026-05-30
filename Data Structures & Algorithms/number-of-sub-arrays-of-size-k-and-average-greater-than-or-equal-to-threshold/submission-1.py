class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        runningSum = 0
        L, subArrCount = 0, 0

        threshold *= k # Avoid division on every iteration
        # And avoids integer division truncation, especially
        # in languages like Go, C++ & Java, since it truncates towards 0.

        for R in range(len(arr)):
            runningSum += arr[R]

            if R - L + 1 == k:
                if runningSum >= threshold: subArrCount += 1

                runningSum -= arr[L]
                L += 1
        
        return subArrCount
            
