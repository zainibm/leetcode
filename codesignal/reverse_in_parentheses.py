'''
Reverse in Parentheses
'''
def reverseInParentheses(s):
	stack = []
	res = ""
	for c in s:
		if c == ")":
			temp = stack.pop()
			while temp != "(":
				res += temp
				temp = stack.pop()
		elif c == "(" or stack:
			stack.append(c)
		else:
			res += c
	return res

print(reverseInParentheses("(bar)")) # rab
print(reverseInParentheses("foo(bar)baz(blim)")) # foorabbazmilb