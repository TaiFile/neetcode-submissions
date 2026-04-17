class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        values = []
        for i in range(len(tokens)):
            if tokens[i] in ("+", "-", "/", "*"):
                temp1 = values.pop()
                temp2 = values.pop()
                if tokens[i] == "+":
                    values.append(temp1 + temp2)
                elif tokens[i] == "-":
                    values.append(temp2 - temp1)
                elif tokens[i] == "/":
                    values.append(int(temp2 / temp1))
                elif tokens[i] == "*":
                    values.append(temp1 * temp2)
            else:
                values.append(int(tokens[i]))
        return values.pop()