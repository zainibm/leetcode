/*
Valid Parentheses
https://leetcode.com/problems/valid-parentheses/
Optimize!
*/
var isValid = function (s) {
  let stack = [];
  for (let i = 0; i < s.length; i++) {
    if (stack[stack.length - 1] === "(" && s[i] === ")") {
      stack.pop();
    } else if (stack[stack.length - 1] === "{" && s[i] === "}") {
      stack.pop();
    } else if (stack[stack.length - 1] === "[" && s[i] === "]") {
      stack.pop();
    } else {
      stack.push(s[i]);
    }
  }
  return stack.length === 0;
};

console.log(isValid("(){}[]")); // true
console.log(isValid("]")); // false
