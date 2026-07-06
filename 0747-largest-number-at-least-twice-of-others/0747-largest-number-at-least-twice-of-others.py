class Solution:
    def dominantIndex(self, nums):
        if len(nums) == 1:
            return 0

        max1 = max(nums)
        index = nums.index(max1)

        nums[index] = -1
        max2 = max(nums)

        return index if max1 >= 2 * max2 else -1