from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        record = {}
        for str in strs:
            sortStr = "".join(sorted(str))
            if sortStr in record:
                record[sortStr].append(str)
            else:
                record[sortStr] = [str]
        return list(record.values())
