from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        record = {}
        for idx, val in enumerate(nums):
            temp = target - val
            if temp not in record:
                record[val] = idx
            else:
                return [record[temp], idx]