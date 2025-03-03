'''
Sqrt(x)
https://leetcode.com/problems/sqrtx/
'''
def mySqrt(x) -> int:
    begin = 1
    end = x
    while begin <= end:
        mid = begin + (end - begin)//2
        sqr = mid * mid
        if sqr == x:
            return mid
        if sqr < x:
            begin = mid + 1
        elif sqr > x:
            end = mid - 1
    return end

print(mySqrt(4)) # 2
print(mySqrt(8)) # 2