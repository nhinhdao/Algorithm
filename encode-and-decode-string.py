'''
    given a list string, encode to a string
    given the above string, decode to original list string
    i.e. ["i", "love", "nami] to "i love nami"
         "i love nami" to ["i", "love", "nami]
    
    solution: space and number alone seem to breaks in edge cases
    we will use length and hash to separate them

    encode
    loop thru the array, count each string and attach len(str)# to front
    i.e ["i", "love", "nami]   = "1#i4#love4#nami"
        ["i", "love", "4#nami] = "1#i4#love6#4#nami

    decode
    loop thru str, count the letter after (number)# and push to array
    i.e 1#i = ["i"], 4#namisan = ["nami"]
'''

def encodeSt(listStr):
    # ["i", "love", "nami"]
    result = ""
    for i in listStr:
        result +=  f"{len(i)}#{i}"

    return result

def decodeSt(str):
    # "1#i4#love4#nami"
    arr = []
    i = 0

    while i < len(str):
        j = i + 1
        while str[j] != '#':
            j += 1

        length = int(str[i:j])
        j += 1

        while i < j:
            arr.append(str[j : j + length])
            i = j + length
        j = i + 1

    return arr

print(encodeSt(["i", "love", "nami", "4#swan"]))
print(decodeSt("1#i4#love4#nami6#4#swan"))
