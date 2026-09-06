def contain_duplicate(nums):

    nums.sort()
    left = 0
    right  = 1

    while right < len(nums):
        if nums[left] == nums[right]:
            return True
        left += 1
        right += 1
    return False




# Test case 1: duplicate exists
print(contain_duplicate([1, 2, 3, 2, 4]))   # expected: True

# Test case 2: duplicate exists at the end
print(contain_duplicate([5, 1, 6, 7, 8, 8]))   # expected: True

# Test case 3: no duplicate
print(contain_duplicate([1, 2, 3, 4, 5]))   # expected: False

# Test case 4: empty array
print(contain_duplicate([]))                 # expected: False

# Test case 5: all elements same
print(contain_duplicate([7, 7, 7, 7]))      # expected: True
    

        

