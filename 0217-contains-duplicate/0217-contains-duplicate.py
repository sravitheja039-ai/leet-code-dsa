class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen=set()
        output=False
        for i in nums:
            if i in seen:
                output=True
            seen.add(i)
        return output
                
            
        