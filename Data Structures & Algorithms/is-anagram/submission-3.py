class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        biggerStr = s if len(s) > len(t) else t
        for char in biggerStr: 
            if s.count(char) != t.count(char): 
                return False
        return True