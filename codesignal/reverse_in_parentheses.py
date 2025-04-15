'''
Reverse in Parentheses
https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses
'''
def reverseInParentheses(s):
	stack = []
	res = ""
	for c in s:
		if c == ")":
			check = stack.pop()
			temp = ""
			while check != "(":
				temp += check
				check = stack.pop()
			if stack:
				for t in temp:
					stack.append(t)
			else:
				res += temp
		elif c == "(" or stack:
			stack.append(c)
		else:
			res += c
	return res

print(reverseInParentheses("(bar)")) # rab
print(reverseInParentheses("foo(bar)baz(blim)")) # foorabbazmilb
print(reverseInParentheses("foo(bar(baz))blim")) # foobazrabblim