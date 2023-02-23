def containDuplicate(arr):
    for idx, x in enumerate(arr):
        if arr.index(x) is not idx:
            return True

    return False

def containDuplicateUsingHash(arr):
    group = {}
    for x in arr:
        if x in group:
            return True
        group[x] = 1
    return False

print(containDuplicateUsingHash([1, 2, 3, -1, -11]))