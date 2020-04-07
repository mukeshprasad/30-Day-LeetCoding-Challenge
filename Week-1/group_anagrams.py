# Group Anagrams

# Given an array of strings, group anagrams together.

## Example:

# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
"""
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
"""
# Note:
# 1  All inputs will be in lowercase.
# 2. The order of your output does not matter.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for i in strs:
            ans[''.join(sorted(i))].append(i)
        return list(ans.values())
