'''
Encode and Decode Strings
https://leetcode.com/problems/encode-and-decode-strings
https://neetcode.io/problems/string-encode-and-decode
'''
def encode(strs):
    encoded = ""
    for s in strs:
        encoded += str(len(s))
        encoded += ","
    encoded += "#"
    encoded = encoded + "".join(strs)
    return encoded

def decode(s):
    s_split = s.split("#", maxsplit=1)
    s_size = s_split[0].split(",")
    decoded = []
    i = 0
    begin = 0
    while s_size[i] != "":
        end = int(s_size[i])
        decoded.append(s_split[-1][begin:begin+end])
        begin += end
        i += 1
    return decoded

encoded = encode(["neet", "code", "love", "you"])
print(encoded) # "4,4,4,3,#neetcodeloveyou"
decoded = decode(encoded)
print(decoded) # ["neet", "code", "love", "you"]

encoded = encode(["1,23", "45,6", "7,8,9"])
print(encoded) # "4,4,5,#1,2345,67,8,9"
decoded = decode(encoded)
print(decoded) # ["1,23", "45,6", "7,8,9"]