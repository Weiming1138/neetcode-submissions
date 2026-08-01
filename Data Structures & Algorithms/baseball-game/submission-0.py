class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for i in range(len(operations)):
            if operations[i] == "+":
                record.append(int(record[-1] + record[-2]))
            elif operations[i] == "D":
                record.append(2 * record[-1])
            elif operations[i] == "C":
                record.pop()
            else:
                record.append(int(operations[i]))
        
        print(record)
        return sum(record)