class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_ = nums[0]
        cur = 0
        for num in nums:
            cur += num
            sum_ = max(cur,sum_)
            if cur < 0:
                cur = 0
            

        return sum_      
        