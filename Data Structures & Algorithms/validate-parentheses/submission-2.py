from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for value in s:
            if value in "({[":
                stack.append(value)
            elif value in ")}]":
                if not stack:
                    # fecha sem ter aberto
                    return False
                top = stack.pop()
                # verifica se o topo fecha corretamente com value
                if (top == "(" and value != ")") or \
                   (top == "{" and value != "}") or \
                   (top == "[" and value != "]"):
                    return False
        return len(stack) == 0