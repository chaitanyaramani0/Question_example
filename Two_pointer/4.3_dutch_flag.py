def dutch_flag(arr):
    i = 0
    j = 1

    while i < len(arr):
        if arr[i] == arr[j]:
            j +=1
            continue

        if arr[i] > arr[j]:
            arr[i],arr[j] = arr[j],arr[i]

        

            
