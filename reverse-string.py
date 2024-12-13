'''
    reverse "I love programing" to "programing love I
'''

def reverseStr(str):
    newStr = str.split(" ")[::-1]
    return (" ").join(newStr)

def reverseStrTheLongWay(str):
    newStr = str.strip().split(" ") # ["i", "love", "program", "so", "ok"]
    i = 0
    j = len(newStr) - 1 # 4

    while j > len(newStr)/2: # (4 vs 2)
        '''
        temp = newStr[i] # "i"
        newStr[i] = newStr[j]
        newStr[j] = temp
        '''
        newStr[i], newStr[j] = newStr[j], newStr[i]
        i += 1
        j -= 1

    return newStr


print(reverseStrTheLongWay("I love programing so so "))