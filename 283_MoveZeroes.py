from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # 想象成补座位的情形, 但难点是i与j以及值变化
        frontZeroIdx = 0  # 定位最前面的0
        for notZeroIdx in range(len(nums)):
            if nums[notZeroIdx] != 0:  # 定位到0后最前面的非零
                nums[frontZeroIdx], nums[notZeroIdx] = nums[notZeroIdx], nums[frontZeroIdx]
                frontZeroIdx += 1  # 保持定位为最前面的0


if __name__ == '__main__':
    nums = [9, 1, 4, 0, 3, -1, 0, 5, 0, -1, 6]
    print(Solution().moveZeroes(nums))
