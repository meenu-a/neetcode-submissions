class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i in range (0, len(nums)):
            complement = target - nums[i]
            if complement in nums_dict:
                return [nums_dict[complement], i]
            else:
                nums_dict[nums[i]] = i