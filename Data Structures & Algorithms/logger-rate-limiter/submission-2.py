class Logger:

    def __init__(self):
        self.rateLimitDict = {} # Store msg: next allowed time

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        # The message strings here are short (30 chars), but in the real world, assuming they're longer
        # and since there could be sensitive information, I'd hash the values
        if message not in self.rateLimitDict:
            self.rateLimitDict[message] = timestamp + 10 # assuming timestamp val is in seconds
            return True
        
        if timestamp >= self.rateLimitDict[message]:
            self.rateLimitDict[message] = timestamp + 10
            return True
        
        return False




# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
