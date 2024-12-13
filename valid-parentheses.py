def isValidParentheses(str):
    # map the close parenthese with the corresponding opening one
    closeToOpen = {
        "}": "{",
        "]": "[",
        ")": "(",
        ">": "<"
    }
    stack = []
    openParenthese = 0
    closeParenthese = 0

    for i in str:
        if i in closeToOpen:
            if stack and stack[-1] == closeToOpen[i]:
                openParenthese -= 1
            else:
                closeParenthese += 1
        else:
            if i in closeToOpen.values():
                stack.append(i)
    
    return len(stack) == 0


print(isValidParentheses("}])>"));
