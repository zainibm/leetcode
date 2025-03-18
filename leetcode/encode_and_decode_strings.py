'''
Encode and Decode Strings
https://leetcode.com/problems/encode-and-decode-strings
https://neetcode.io/problems/string-encode-and-decode
Implement decode(s)
'''
def encode(strs):
    encoded = ""
    for s in strs:
        encoded += str(len(s))
        encoded += ","
    encoded += "#"
    encoded = encoded + "".join(strs)
    return encoded

'''
def decode(s):
    s_split = s.split(",")
    decoded = []
    i = 0
    begin = 1
    while s_split[i][0] != "#":
        end = int(s_split[i])
        decoded.append(s_split[-1][begin:begin+end])
        begin += end
        i += 1
    return decoded
'''

print(encode(["neet", "code", "love", "you"])) # "4,4,4,3,#neetcodeloveyou"
print(encode(["1,23", "45,6", "7,8,9"])) # "4,4,5,#1,2345,67,8,9"