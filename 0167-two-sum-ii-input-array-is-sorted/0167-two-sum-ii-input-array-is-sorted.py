class Solution:
    def twoSum(self, a: List[int], target: int) -> List[int]:
        i=0
        j=len(a)-1
        while i<j:


            current=a[i]+a[j]

            if current==target:

                 return [i+1,j+1]
                 break
            elif current>target:
                  j-=1
            else:
                  i+=1
        
