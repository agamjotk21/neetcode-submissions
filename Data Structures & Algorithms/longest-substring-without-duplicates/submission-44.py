class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '': return 0
        elif len(s) == 1: return 1
        best = 0
        l = 0
        curr = set()
        for r in range(len(s)):
            if s[r] not in curr: 
                curr.add(s[r])
            else:
                best = max(len(curr), best)
                while s[r] in curr: 
                    curr.remove(s[l])
                    l+=1
                curr.add(s[r])
            
        best = max(len(curr), best)
        return best


