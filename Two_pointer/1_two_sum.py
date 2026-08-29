
# find only one pair if it ask to find all posible pair solution is TODO
def two_sum(array,target):
    #if que. ask to return number it self you can sort array but if they ask idex you can not sort array. this qustion is for number,
    arr = sorted(array)
    i = 0
    j = len(arr)-1

    while(i<j):
        if arr[i] + arr[j] == target:
            return {arr[i],arr[j]}
        elif arr[i]+ arr[j] < target:
            i += i 
        else:
            j -= j
    return None


arr = [7,2,4,9,5,7,9]
target = 98

print(two_sum(arr,target))

 