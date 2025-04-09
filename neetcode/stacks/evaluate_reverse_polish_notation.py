'''
Evaluate Reverse Polish Notation
https://leetcode.com/problems/evaluate-reverse-polish-notation
https://neetcode.io/problems/evaluate-reverse-polish-notation
'''
def evalRPN(tokens) -> int:
    stack = []
    operations = ["+", "-", "*", "/"]
    for token in tokens:
        if token not in operations:
            stack.append(token)
        else:
            f_operand = stack.pop()
            l_operand = stack.pop()
            total = 0
            if token == "+":
                total = int(f_operand) + int(l_operand)
            elif token == "-":
                total = int(l_operand) - int(f_operand)
            elif token == "*":
                total = int(f_operand) * int(l_operand)
            elif token == "/":
                total = int(l_operand) / int(f_operand)
            stack.append(total)
    return int(stack.pop())

print(evalRPN(["2", "1", "+", "3", "*"])) # 9
print(evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])) # 22