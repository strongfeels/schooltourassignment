class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if s[0] not in ["{","[","("]:
            return False
        for i in range(len(s)):
            if s[i] in ["{","[","("]:
                stack.append(s[i])
        if s[i] in ["}","]",")"]:
            if s[i] == "}":
                if stack[-1] == "{":
                    stack.pop()
            if s[i] == "]":
                if stack[-1] == "[":
                    stack.pop()
            if s[i] == ")":
                if stack[-1] == "(":
                    stack.pop()
            if stack == []:
                 return True
            else:
                 return False