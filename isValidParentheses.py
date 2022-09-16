
""" 
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
"""

def isValidParentheses(str):
    # map the close parenthese with the corresponding opening one
    closeToOpen = {
        "}": "{",
        "]": "[",
        ")": "("
    }

    # declare an empty stack
    stack = []

    # {}()[]
    for s in str:
        # if it is a close pr
        if s in closeToOpen:
            # if there is a matching open pr in the stack, remove the open pr from stack
            if stack and (stack[-1] == closeToOpen[s]):
                stack.pop()
                # else return false because the close pr doesn't have a matching open one
            else:
                return False
            # if it is an open pr, add it to the stack
        else:
            stack.append(s) 

    # return true if the stack is empty
    return len(stack) == 0


print(isValidParentheses("{}(])[]"));
