'''
Two Sum
https://leetcode.com/problems/two-sum
https://neetcode.io/problems/two-integer-sum
'''
def twoSum(nums, target):
    dict = {}
    for index, num in enumerate(nums):
        if target - num in dict:
            return [dict[target-num], index]
        else:
            dict[num] = index

print(twoSum([2, 7, 11, 15], 9)) # [0, 1]
print(twoSum([3, 2, 4], 6)) # [1, 2]

'''
Alternatively:
def twoSum(nums, target) :
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                if i < j:
                    return [i, j]
                else:
                    return [j, i]
'''