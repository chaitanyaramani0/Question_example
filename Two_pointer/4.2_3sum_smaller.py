def three_sum_smaller(nums,target):
    nums.sort()
    no_of_triplet = 0

    for i in range(len(nums)-2):
        left  = i + 1
        right = len(nums)-1

        while (left < right):
            s = nums[i]+nums[left]+nums[right]

            if s < target:
                no_of_triplet = no_of_triplet + (right-left)
                left += 1
            else:
                right -= 1

    return no_of_triplet


tests = [
    ([-2, 0, 1, 3], 2, 2),      # valid triplets: (-2,0,1), (-2,0,3)
    ([-2, 0, 1, 3], 3, 3),      # valid triplets: (-2,0,1), (-2,0,3), (-2,1,3)
    ([1, 2, 3, 4], 10, 4),      # valid triplets: (1,2,3),(1,2,4),(1,3,4),(2,3,4)
    ([0, 0, 0], 0, 0),          # no triplet has sum < 0
    ([-5, -4, -3, -2, -1], -10, 10),  # all combos under target
    ([], 0, 0),                 # empty list
    ([5, 5, 5], 15, 0),         # sum == target, not less than
    ([1, 1, 1, 1], 3, 0),       # all triplets = 3, should be 0 because 3 < 3 is false
]

for nums, target, expected in tests:
    result = three_sum_smaller(nums, target)
    print(f"nums={nums}, target={target}, result={result}, expected={expected}, PASS={result == expected}")