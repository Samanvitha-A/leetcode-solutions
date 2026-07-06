class Solution:
    def findDuplicates(self, nums):
        ans = []

        for num in nums:
            index = abs(num) - 1

            if nums[index] < 0:
                ans.append(abs(num))
            else:
                nums[index] = -nums[index]

        return ans
        