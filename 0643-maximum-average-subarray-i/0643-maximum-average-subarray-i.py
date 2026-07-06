class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        windowsum=0
        windowsum1=0
        for i in range(k):
            windowsum+=nums[i]
            windowsum1=windowsum/k
            
        maxAvr=0
        for i in range(k,len(nums)):
            windowsum=windowsum-nums[i-k]+nums[i]
            maxAvr=windowsum/k
            if windowsum1<maxAvr:
                windowsum1=maxAvr
        return windowsum1
        

            
        