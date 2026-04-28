class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        sDict = dict()
        for l in s:
            if l in sDict:
                sDict[l] += 1
            else:
                sDict[l] = 1
        
        tDict = dict()
        for l in t:
            if l in tDict:
                tDict[l] += 1
            else:
                tDict[l] = 1
        
        return sDict == tDict
        