'''
First Unique Character in a String
https://leetcode.com/problems/first-unique-character-in-a-string
'''
from collections import deque

def firstUniqChar(s) -> int:
    q = deque()
    dict = {}
    for i in range(len(s)):
        if s[i] not in dict:
            q.append(i)
            dict[s[i]] = 1
        else:
            dict[s[i]] += 1
    while q:
        index = q.popleft()
        if dict[s[index]] == 1:
            return index
    return -1

print(firstUniqChar("leetcode")) # 0
print(firstUniqChar("aabb")) # -1