class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d_nums={nums[i]:i for i in range(len(nums))}

        for i in range(len(nums)):
            match_num=target-nums[i]
            if match_num in d_nums:
                if i!=d_nums[match_num]:
                    return [i,d_nums[match_num]]