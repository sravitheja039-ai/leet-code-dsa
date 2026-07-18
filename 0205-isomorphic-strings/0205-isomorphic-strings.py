class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        h={}
        v={}
        for i in range(len(s)):
            ch1=s[i]
            ch2=t[i]
            if ch1 in h:
                if h[ch1]!=ch2:
                    return False
            else:
                h[ch1]=ch2
            if ch2 in v:
                if v[ch2]!=ch1:
                    return False
            else:
                v[ch2]=ch1
        return True
        
                    
           

        
                
        
        