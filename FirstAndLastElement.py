# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].







#  Two-Pointer Approach:
# Initialize two pointers, left and right, to the beginning and end of the array, respectively.
# Initialize two variables, first and last, to -1.
# Use a while loop with the condition left <= right.
# Calculate the middle index as (left + right) / 2.
# If the middle element is equal to the target, update first and last accordingly and adjust the pointers.
# If the middle element is less than the target, update left.
# If the middle element is greater than the target, update right.
# Continue the loop until left is less than or equal to right.
# Return first and last.







class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        first, last = -1, -1
        
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                first = mid
                last = mid
                while first > 0 and nums[first - 1] == target:
                    first -= 1
                while last < len(nums) - 1 and nums[last + 1] == target:
                    last += 1
                return [first, last]
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return [first, last]
