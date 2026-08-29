def three_sum_closest_target(nums,target):
    nums.sort()
    closest_sum = float('inf')
    for i in range(len(nums)-2):
        left = i + 1
        right  = len(nums)-1

        while (left < right):
            s = nums[i] + nums[left] + nums[right]
    
            if abs(s - target) < abs(closest_sum - target):
                closest_sum = s
            if s == target:
                return s
            elif s < target:
                left += 1
            elif s > target:
                right -= 1
    return closest_sum


three_sum_closest_target([0,0,0],1)