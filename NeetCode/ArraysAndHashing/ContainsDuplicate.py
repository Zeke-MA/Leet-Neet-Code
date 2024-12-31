from typing import List
'''
https://neetcode.io/problems/duplicate-integer
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true

Example 2:

Input: nums = [1, 2, 3, 4]

Output: false
'''
# One line solution - if we convert the input list to a set it will remove duplicate values
# If the input list length is the same as the set, the input list must contain all unique values
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return not len(set(nums)) == len(nums)
    

solution = Solution()

print(solution.hasDuplicate([1, 2, 3, 4]))
print(solution.hasDuplicate([1, 2, 2, 3]))
print(solution.hasDuplicate([5, 5, 5, 5]))
print(solution.hasDuplicate([10, 20, 30]))