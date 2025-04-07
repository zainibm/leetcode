'''
Valid Parentheses
https://leetcode.com/problems/valid-parentheses
https://neetcode.io/problems/validate-parentheses
'''
def isValid(s) -> bool:
    stack = []
    pairs = {")": "(", "}": "{", "]": "["}
    for c in s:
        if c in pairs:
            if stack and stack[-1] == pairs[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    return len(stack) == 0

print(isValid("()[]{}")) # True
print(isValid("(]")) # False