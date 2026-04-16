class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        dice = {}

        if len(s) != len(t):
            return False

        for char in s:
            dice[char] = dice.get(char,0)+1

        for char in t:
            if char not in dice:
                return False

            if char in dice:
                dice[char] -= 1

            if dice[char] < 0:
                return False

        return True

            
        