class Solution:
    from typing import List 
    def sortedSquares(self, nums: List[int]) -> List[int]:

        pos = []
        nag = []
        result = []

        for i in nums:
            pos.append(i) if i >= 0 else nag.append(i)
            # if i >= 0:
            #     pos.append(i)
            # else:
            #     nag.append(i)

        if len(nag) == 0:
            return [x*x for x in pos]
        
        if len(pos) == 0:
            return [x*x for x in nag][::-1]

        n = len(nag)
        m = len(pos)
        i , j = 0 ,0
        # j = 0

        pos = [x*x for x in pos]
        neg = [x*x for x in nag][::-1]
    
        while (i < n and j < m):
            if neg[i] < pos[j]:
                result.append(neg[i])
                i += 1
            else:
                result.append(pos[j])
                j += 1

        while i < n:
            result.append(neg[i])
            i += 1
        while j < m:
            result.append(pos[j])
            j += 1
        
        return result 

