from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)  # [-4, -1, -1, 0, 1, 2]
        record = []
        m = 1
        r = len(nums) - 1
        for i in range(len(nums)):
            temp = nums[r]
            if nums[i] + nums[m] == temp:
                record.append([nums[i], nums[m], temp])
            elif  nums[i] + nums[m] >= 0:
                return record
            elif nums[i] + nums[m] < temp:
                i += 1
                continue
            else: r -= 1


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    s = Solution()
    print(s.threeSum(nums))
