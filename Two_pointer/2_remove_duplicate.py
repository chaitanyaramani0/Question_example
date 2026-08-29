def remove_duplicate(array):
    i = 0
    j = 1
    res = 1
    while j < len(array):
        if array[j] == array[i]:
            j += 1
            continue
        array[i+1] = array[j]
        i += 1
        res += 1
        j += 1
    return res



print(remove_duplicate([1,1,1,5,5,9,10,10,10,12,12,13]))