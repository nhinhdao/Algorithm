def calPoints(operations):
    temp = []
    
    for i in operations:
        if i == "C":
            temp.pop()
        elif i == "D":
            num = temp[-1]*2
            temp.append(num)
        elif i == "+":
            temp.append(temp[-1] + temp[-2])
        else:
            temp.append(int(i))
                
    return sum(temp)