'''
Top K Frequent Elements
https://leetcode.com/problems/top-k-frequent-elements
https://neetcode.io/problems/top-k-elements-in-list
Implement bucket sort!
'''
def topKFrequent(nums, k):
    dict = {}
    for num in nums:
        if num in dict:
            dict[num] += 1
        else:
            dict[num] = 1
    arr = list(dict.items())
    arr = sorted(arr, key=lambda x: x[1])
    freq = []
    while len(freq) < k:
        freq.append(arr.pop()[0])
    return freq

print(topKFrequent([1, 1, 1, 2, 2, 3], 2)) # [2, 3]
print(topKFrequent([1], 1)) # [1]