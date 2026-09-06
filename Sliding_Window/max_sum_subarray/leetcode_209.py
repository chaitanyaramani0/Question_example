####################################################################################################################################################################################################################
# """GIVEN AN ARRAY OF POSITIVE INTEGERS NUMS AND A POSITIVE INTEGER TARGET, RETURN THE MINIMAL LENGTH OF A SUBARRAY WHOSE SUM IS GREATER THAN OR EQUAL TO TARGET. IF THERE IS NO SUCH SUBARRAY, RETURN 0 INSTEAD. #
#                                                                                                    EXAMPLE 1:                                                                                                    #
#                                                                                     INPUT: TARGET = 7, NUMS = [2,3,1,2,4,3]                                                                                      #
#                                                                                                    OUTPUT: 2                                                                                                     #
#                                                               EXPLANATION: THE SUBARRAY [4,3] HAS THE MINIMAL LENGTH UNDER THE PROBLEM CONSTRAINT.                                                               #
#                                                                                                    EXAMPLE 2:                                                                                                    #
#                                                                                        INPUT: TARGET = 4, NUMS = [1,4,4]                                                                                         #
#                                                                                                    OUTPUT: 1                                                                                                     #
#                                                                                                    EXAMPLE 3:                                                                                                    #
#                                                                                   INPUT: TARGET = 11, NUMS = [1,1,1,1,1,1,1,1]                                                                                   #
#                                                                                                    OUTPUT: 0                                                                                                     #
#                                                                                                       """                                                                                                        #
####################################################################################################################################################################################################################


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        low = 0
        high = 0
        current_sum = 0 
        min_window = float('inf')

        while high < len(nums):
            current_sum += nums[high]
            high += 1

            while current_sum >= target: 
                min_window = min(min_window,high-low)
                current_sum -= nums[low]
                low += 1
        
        return min_window if min_window != float('inf') else 0
        

#second approch

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        res = float("inf")
        summ  = 0
        i = 0

        for j in range(len(nums)):
            summ += nums[j]

            while summ >= target:
                res = min(res, j - i + 1)
                summ -= nums[i]
                i += 1
        
        return res if res != float("inf")  else 0