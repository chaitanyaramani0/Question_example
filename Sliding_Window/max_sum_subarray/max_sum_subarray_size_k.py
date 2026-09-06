def max_sum_subarray(arr,k):
    low = 0
    high = k-1
    total_sum = 0
    max_sum = 0
    for i in range(low,k):
        total_sum = total_sum + arr[i]

    while high < len(arr):
        max_sum = max(total_sum,max_sum)
        low += 1
        high += 1

        if high == len(arr):
            break

        total_sum = total_sum -arr[low-1] 
        total_sum = total_sum + arr[high]

    return max_sum


# def max_sum_subarray(arr,k):
#     n = len(arr)
#     if n < k:
#         return 0

#     window_sum = sum(arr[:k])
#     max_sum = window_sum

#     for i in range(k, n):
#         window_sum += arr[i] - arr[i - k]
#         max_sum = max(max_sum, window_sum)

#     return max_sum



test_cases = [
    ([2, 1, 5, 1, 3, 2], 3, 9),
    ([2, 3, 4, 1, 5], 2, 7),
    ([-2, -1, -3, -4], 2, -3),
    ([5, 5, 5, 5], 4, 20),
]

for arr, k, expected in test_cases:
    result = max_sum_subarray(arr, k)
    print(f"Input: arr={arr}, k={k}")
    print(f"Expected: {expected}, Got: {result}")
    print("Passed" if result == expected else "Failed")
    print()