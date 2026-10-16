class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ''
        for char in s: 
            if char.isalnum():
                newS += char.lower()
        right = len(newS) - 1
        left = 0

        while right > left: 
            if newS[right] == newS[left]: 
                right -= 1
                left += 1
            else: 
                return False
        return True

        