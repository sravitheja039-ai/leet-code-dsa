class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words=s.split()
        if len(pattern)!=len(words):
            return False
        h={}
        v={}
        for i in range(len(pattern)):
            ch=pattern[i]
            word=words[i]
            if ch in h:
                if h[ch]!=word:
                    return False
            else:
                h[ch]=word
            if word in v:
                if v[word]!=ch:
                    return False
            else:
                v[word]=ch
        return True
       
