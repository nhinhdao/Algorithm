def printVals(head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    
    print(arr)
