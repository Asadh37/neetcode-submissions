class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        for a in s:
            if a.isalnum():
                clean += a

        clean = clean.lower()
        left = 0
        right  = len(clean) - 1

        while(left < right):
            if clean[left] != clean[right]:
                return False
            left+=1
            right-=1
        return True    
        