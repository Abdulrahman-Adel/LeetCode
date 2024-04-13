class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = "".join(c for c in s if c.isalnum())
        
        pointer1 = 0
        pointer2 = len(s) - 1
        
        while pointer1 < pointer2:
            char1, char2 = s[pointer1], s[pointer2]
            if char1 != char2:
                return False
            pointer1 += 1
            pointer2 -= 1
            
        return True