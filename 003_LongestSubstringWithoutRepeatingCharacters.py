from builtins import str


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        record = set()
        l = res = 0
        for r in range(len(s)):
            while s[r] in record:
                record.remove(s[l])
                l += 1
            record.add(s[r])
            res = res if (r - l + 1) < res else (r - l + 1)

        return res


if __name__ == '__main__':
    str = 'asdgfhassfbv'
    # for i in str:
        # print(i)
    s = Solution()
    print(s.lengthOfLongestSubstring(str))
