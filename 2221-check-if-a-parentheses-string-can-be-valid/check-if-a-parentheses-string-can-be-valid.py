class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        stack_lock = []
        stack_unlock = []

        for i in range(len(s)):
            if locked[i] == "0":
                stack_unlock.append(i)
            elif s[i] == "(" :
                stack_lock.append(i)
            else:
                if stack_lock:
                    stack_lock.pop()
                elif stack_unlock:
                    stack_unlock.pop()
                else:
                    return False
        while stack_lock and stack_unlock and stack_lock[-1] < stack_unlock[-1]:
            stack_lock.pop()
            stack_unlock.pop()
        if stack_lock:
            return False
        
        return True if len(stack_unlock) % 2 == 0 else False
