# 1.
# Given an integer array nums, return true if any value appears at least twice in the array,
# and return false if every element is distinct.

def contains_duplicate(nums: list) -> bool:
    nums_set = set(nums)
    return len(nums) > len(nums_set)




