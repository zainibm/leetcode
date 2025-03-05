'''
Contains Duplicate
https://leetcode.com/problems/contains-duplicate
https://neetcode.io/problems/duplicate-integer
'''
def containsDuplicate(nums) -> bool:
    dict = {}
    for num in nums:
        if num in dict:
            return True
        else:
            dict[num] = 1
    return False

print(containsDuplicate([1, 2, 3, 4])) # False
print(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])) # True