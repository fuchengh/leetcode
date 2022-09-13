class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for c in s:
            if c == ")":
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if top != "(":
                    return False
            if c == "]":
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if top != "[":
                    return False
            if c == "}":
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if top != "{":
                    return False
            if c in "([{":
                stack.append(c)
        
        if len(stack) != 0:
            return False
        return True