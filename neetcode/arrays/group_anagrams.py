'''
Group Anagrams
https://leetcode.com/problems/group-anagrams
https://neetcode.io/problems/anagram-groups
'''
def groupAnagrams(strs):
    dict = {}
    for str in strs:
        sorted_str = "".join(sorted(str))
        if sorted_str in dict:
            dict[sorted_str].append(str)
        else:
            dict[sorted_str] = [str]
    return list(dict.values())

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])) # [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
print(groupAnagrams([""])) # [[""]]