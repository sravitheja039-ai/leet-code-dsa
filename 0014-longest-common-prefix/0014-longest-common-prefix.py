class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        for i in range(len(strs[0])):

            for j in range(1, len(strs)):

                # If current string is shorter
                # OR characters don't match
                if i >= len(strs[j]) or strs[0][i] != strs[j][i]:
                    return strs[0][:i]

        return strs[0]