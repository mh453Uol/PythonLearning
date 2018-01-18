#https://www.freecodecamp.org/challenges/diff-two-arrays

# compare two array and return a 
# new array with any items only found 
# in one of the two given arrays

def diffArray(arr1,arr2):
    difference = []

    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] == arr2[j]:
                arr1[i] = None
                arr2[j] = None
                break
    print(arr1,arr2)

    for el in arr1:
        if el:
            difference.append(el)
    
    for el2 in arr2:
        if el2:
            difference.append(el2)
    
    return difference

print(diffArray([4,"MAjid"],[1,2,3,4,5,"MAjid"]))
                        