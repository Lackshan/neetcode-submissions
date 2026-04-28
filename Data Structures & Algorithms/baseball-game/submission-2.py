class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for op in operations:
            if op == "C":
                record.pop() # constraint specifies there will always be a val before
            elif op == "D":
                record.append(record[-1] * 2)
            elif op == "+":
                record.append(record[-1] + record [-2])
            else: # Avoid reflection by using else instead of doing type check for int
                record.append(int(op))
        
        return sum(record)
            
