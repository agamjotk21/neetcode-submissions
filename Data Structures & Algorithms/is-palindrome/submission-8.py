class Solution:
    import string
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        newS = ''.join(char for char in s if char.isalnum())
        print
        j = len(newS) - 1
        for i in range(len(newS)): 
            if newS[i] != newS[j]: 
                return False 
            j -= 1
        
        return True