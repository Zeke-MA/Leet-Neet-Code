from typing import List
'''
https://neetcode.io/problems/two-integer-sum

Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.

Example 1:

Input: 
nums = [3,4,5,6], target = 7

Output: [0,1]
Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

Example 2:

Input: nums = [4,5,6], target = 10

Output: [0,2]
Example 3:

Input: nums = [5,5], target = 10

Output: [0,1]

'''
# The possible dictionary is created to store the values we haev already seen and at what index
# Then we loop over the input nums list, at the current index i we can calculate what number we need by taking it away from the target
# Since we now know what number we need, we check our dictionary to check if we have see the number yet. If we have return the list of the two indexes
# If we have not seen it add the number at the current index as a new key and the index as a value
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        possible = {}

        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in possible:
                return [min(i,possible[needed]),max(i,possible[needed])]
            else:
                possible[nums[i]] = i
            
solution = Solution()

print(solution.twoSum([3,4,5,6], 7))
print(solution.twoSum([4,5,6], 10))
print(solution.twoSum([5, 5], 10))