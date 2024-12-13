# transfrom string
#    fox10trot2
#    foxfoxfoxfoxfoxfoxfoxfoxfoxfoxtrottrot

def decodeString(str):
    '''
    fox10trot2
    loop through the str from i (starts at 0)
    increment i until a number, save the index of the number to j
        save the word str [i:j]
        move i = j

    increment j until a letter
    
    concat the word 
        result = word * int(ij)
    '''
    result = ''
    word = ''
    i = 0

    # fox10trot2
    # i
    #    j
    while i < len(str):
        j = i + 1
        while j < len(str) and not str[j].isdigit():
            j += 1
        
        word = str[i:j] # fox
        i = j
        j = i + 1

        while i < j:
            result += word * int(str[i:j+1]) # fox * 10
            i = j + 1 # i = t


    return result
    

print(decodeString("fox10top5"))