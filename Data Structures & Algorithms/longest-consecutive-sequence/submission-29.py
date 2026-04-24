class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums_set  =  set(nums)
        len_  = 0 

        for num in nums_set:
            if num-1 not in nums_set:
                curr = num
                curr_len = 1
                while curr+1 in nums_set:
                    curr_len += 1
                    curr += 1
                len_ = max(curr_len,len_) 
        return len_

            
        