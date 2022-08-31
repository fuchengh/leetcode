class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for c in s:
            if c == "(":
                stack.append(c)
            if c == ")":
                if stack:
                    top = stack.pop()
                    if top != "(":
                        return False
                else:
                    return False
            if c == "[":
                stack.append(c)
            if c == "]":
                if stack:
                    top = stack.pop()
                    if top != "[":
                        return False
                else:
                    return False
            if c == "{":
                stack.append(c)
            if c == "}":
                if stack:
                    top = stack.pop()
                    if top != "{":
                        return False
                else:
                    return False
        
        if stack:
            return False
        return True            