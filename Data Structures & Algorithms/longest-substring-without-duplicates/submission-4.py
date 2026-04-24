class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set_s = set()
        longest = 0

        left = 0

        for right in range(len(s)):
            while (s[right] in set_s):
                set_s.remove(s[left])
                left+=1
            if(s[right] not in set_s):
                set_s.add(s[right])

            longest = max(longest,right-left+1)
        return longest    

            
            




        