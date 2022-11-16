# 1.
# Given an integer array nums, return true if any value appears at least twice in the array,
# and return false if every element is distinct.

def contains_duplicate(nums: list) -> bool:
    nums_set = set(nums)
    return len(nums) > len(nums_set)


# Given an integer array nums,
# find the subarray which has the largest sum and return its sum.

def maximum_subarray(nums: list) -> int:
    newNum = maxTotal = nums[0]

    for i in range(1, len(nums)):
        newNum = max(nums[i], nums[i] + newNum)
        maxTotal = max(newNum, maxTotal)

    return maxTotal


def main():
    arr = [-2, +1, -1, 5, 7]
    n = len(arr)

    max_sum = maximum_subarray(arr)
    print("Maximum contiguous sum is ", max_sum)


if __name__ == '__main__':
    main()

