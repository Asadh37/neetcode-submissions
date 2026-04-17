class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        num_set = set(nums)
        max_len = 0
        current = 0

        if(len(nums)==0):
            return 0

        for num in num_set :
            if num-1 not in num_set:
                current = num
                len_ = 1

                while current+1 in num_set:
                    current += 1
                    len_ += 1
                max_len = max(max_len,len_)
        
        return max_len