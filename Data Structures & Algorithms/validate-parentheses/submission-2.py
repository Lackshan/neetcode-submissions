class Solution:
    def isValid(self, s: str) -> bool:
        # Create the constants that we need
        openBrackets = ["(", "{", "["]
        closeBrackets = [")", "}", "]"]
        bracketDict = {"(": ")", "{": "}", "[": "]"}

        openBracketStack = []

        for char in s:
            if char in openBrackets:
                openBracketStack.append(char)
            if char in closeBrackets:
                if len(openBracketStack) == 0 or char != bracketDict[openBracketStack.pop()]:
                    return False
        
        # This means there are unclosed brackets
        if len(openBracketStack) != 0: return False

        return True
