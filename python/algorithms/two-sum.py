# Time:  O(n)
# Space: O(n)

# Given an array of integers, return indices of the two numbers
# such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution.
#
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


class Solution(object):
    def twoSum(self, nums, target):
        """
        Args:
            nums (TYPE): List[int]
            target (TYPE): int

        Returns:
            TYPE: List[int]
        """

        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return [lookup[target - num], i]
            lookup[num] = i


if __name__ == '__main__':
    print (Solution().twoSum((2, 7, 11, 15, 18), 22))
