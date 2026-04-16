class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        hashmap = {}

        for i in range (len(nums)):
            duplicate = nums[i]
            if duplicate in hashmap:
                return True

            hashmap[nums[i]] = 1 
        return False