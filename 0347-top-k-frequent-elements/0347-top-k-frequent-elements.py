class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h={}
        for i in nums:
            if i in h:
                h[i]+=1
            else:
                h[i]=1
        ans=[]
        for key,values in h.items():
            ans.append((values,key))
        ans.sort(reverse=True)
        arr=[]
        for i in range(k):
            arr.append(ans[i][1])
        return arr

        