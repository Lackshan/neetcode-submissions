class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strsDict = {}

        for word in strs:
            wordKey = tuple(sorted(word))
            if wordKey in strsDict:
                strsDict[wordKey].append(word)
            else:
                strsDict[wordKey] = [word]
        
        return list(strsDict.values())
