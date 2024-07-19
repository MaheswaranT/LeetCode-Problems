'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".


Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''

class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        strs.sort()
        
        first = strs[0]
        last = strs[-1]
        i = 0
        
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1
        
        return first[:i]

