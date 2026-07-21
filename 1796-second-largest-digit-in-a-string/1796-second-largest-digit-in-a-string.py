class Solution:
    def secondHighest(self, s: str) -> int:
        digit=[]
        for ch in s:
            if ch.isdigit():
                digit.append(int(ch))
        digit=sorted(set(digit))
        if len(digit)<2:
            return -1
        return digit[-2]