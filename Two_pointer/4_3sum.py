################################################################################################################################################################
# GIVEN AN INTEGER ARRAY NUMS, RETURN ALL THE TRIPLETS [NUMS[I], NUMS[J], NUMS[K]] SUCH THAT I != J, I != K, AND J != K, AND NUMS[I] + NUMS[J] + NUMS[K] == 0. #
#                                              NOTICE THAT THE SOLUTION SET MUST NOT CONTAIN DUPLICATE TRIPLETS.                                               #
#                                                                          EXAMPLE 1:                                                                          #
#                                                                INPUT: NUMS = [-1,0,1,2,-1,-4]                                                                #
#                                                                 OUTPUT: [[-1,-1,2],[-1,0,1]]                                                                 #
#                                                                         EXPLANATION:                                                                         #
#                                                       NUMS[0] + NUMS[1] + NUMS[2] = (-1) + 0 + 1 = 0.                                                        #
#                                                       NUMS[1] + NUMS[2] + NUMS[4] = 0 + 1 + (-1) = 0.                                                        #
#                                                      NUMS[0] + NUMS[3] + NUMS[4] = (-1) + 2 + (-1) = 0.                                                      #
#                                                      THE DISTINCT TRIPLETS ARE [-1,0,1] AND [-1,-1,2].                                                       #
#                                      NOTICE THAT THE ORDER OF THE OUTPUT AND THE ORDER OF THE TRIPLETS DOES NOT MATTER.                                      #
#                                                                          EXAMPLE 2:                                                                          #
#                                                                    INPUT: NUMS = [0,1,1]                                                                     #
#                                                                          OUTPUT: []                                                                          #
#                                                 EXPLANATION: THE ONLY POSSIBLE TRIPLET DOES NOT SUM UP TO 0.                                                 #
#                                                                          EXAMPLE 3:                                                                          #
#                                                                    INPUT: NUMS = [0,0,0]                                                                     #
#                                                                      OUTPUT: [[0,0,0]]                                                                       #
#                                                     EXPLANATION: THE ONLY POSSIBLE TRIPLET SUMS UP TO 0.                                                     #
#                                                                         CONSTRAINTS:                                                                         #
#                                                                   3 <= NUMS.LENGTH <= 3000                                                                   #
#                                                                    -105 <= NUMS[I] <= 105                                                                    #
################################################################################################################################################################



def threeSum(nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        for i in range(0,len(nums)-2):
            left = i + 1
            right = len(nums) - 1
            s = -nums[i]

            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            while(left < right):
                sums = nums[left] + nums[right]

                if sums == s : 
                    result.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -= 1

                    while left < len(nums) and nums[left] == nums[left-1]:
                        left += 1
                    while right >= 0 and nums[right] == nums[right+1]:
                        right -= 1

                elif sums > s:
                    right -= 1
                else : 
                    left += 1
        return result   