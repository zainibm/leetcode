'''
Valid Anagram
https://leetcode.com/problems/valid-anagram
https://neetcode.io/problems/is-anagram
'''
def isAnagram(s, t) -> bool:
    if (len(s) != len(t)):
        return False
    dict_s = {}
    dict_t = {}
    for i in range(len(s)):
        if s[i] in dict_s:
            dict_s[s[i]] += 1
        elif s[i] not in dict_s:
            dict_s[s[i]] = 0
        if t[i] in dict_t:
            dict_t[t[i]] += 1
        elif t[i] not in dict_t:
            dict_t[t[i]] = 0
    return dict_s == dict_t

print(isAnagram("anagram", "nagaram")) # True
print(isAnagram("rat", "car")) # False

'''
Alternatively:
def isAnagram(s, t) -> bool:
    sorted_s = sorted(s)
    sorted_t = sorted(t)
    s_str = "".join(sorted_s)
    t_str = "".join(sorted_t)
    return s_str == t_str
'''