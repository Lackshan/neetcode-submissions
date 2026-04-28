class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = [0] * n # Initialise answer list

        rightMax = -1 # Since we know the last element is always -1
        for i in range (n - 1, -1, -1):
            ans[i] = rightMax
            if arr[i] > rightMax:
                rightMax = arr[i]

        return ans


