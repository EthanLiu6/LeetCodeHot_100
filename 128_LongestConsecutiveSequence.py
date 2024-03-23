from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        maxSeq = 1
        for num in setNums:
            if (num - 1) not in setNums:
                startNum = num
                seq = 1
                while startNum + 1 in setNums:
                    startNum += 1
                    seq += 1
                maxSeq = max(seq, maxSeq)
        return maxSeq


if __name__ == '__main__':
    nums = [9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]
    print(Solution().longestConsecutive(nums))
