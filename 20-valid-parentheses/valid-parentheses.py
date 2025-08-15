class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        cmatch = { ")" : "(" , 
                    "}" : "{",
                    "]" : "["}
        
        for c in s:
            if c in cmatch :
                if stack and stack[-1] == cmatch[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False


        