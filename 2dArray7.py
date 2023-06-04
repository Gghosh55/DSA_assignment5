def find_min(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        middle = (left + right) // 2

        if nums[middle] > nums[right]:
            left = middle + 1
        else:
            right = middle

    return nums[left]
nums = [3, 4, 5, 1, 2]
print(find_min(nums))
