class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        windowsum=0
        windowsum1=0
        for i in range(k):
            windowsum+=nums[i]
            
            
        maxAvr=windowsum
        for i in range(k,len(nums)):
            windowsum=windowsum-nums[i-k]+nums[i]

            if windowsum>maxAvr:
                maxAvr=windowsum
        return maxAvr/k
        

            
        