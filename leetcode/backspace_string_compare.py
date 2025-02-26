'''
Backspace String Compare
https://leetcode.com/problems/backspace-string-compare
'''
def backspaceCompare(s, t) -> bool:
    new_s = check(s)
    new_t = check(t)
    if new_s == new_t:
        return True
    else:
        return False

def check(str):
    new_str = ""
    skip = 0
    for i in range(len(str)-1, -1, -1):
        if str[i] == "#":
            skip += 1
        else:
            if skip == 0:
                new_str += str[i]
            else:
                skip -= 1
    return new_str

s = "ab#c"
t = "ad#c"
print(backspaceCompare(s, t)) # True

q = "ab##"
r = "c#d#"
print(backspaceCompare(q, r)) # True