from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        left = 0
        right = len(height) - 1
        while right > left:
            area = (height[left] if height[left] < height[right] else height[right]) * (right - left)
            maxArea = area if area > maxArea else maxArea
            if height[left] < height[right]:
                left += 1
                continue
            else:
                right -= 1
                continue
        return maxArea


if __name__ == '__main__':
    heights = [1, 3, 2, 5, 25, 24, 5]
    s = Solution()
    print(s.maxArea(heights))
