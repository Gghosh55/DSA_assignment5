def sorted_squares(nums):
    result = []
    for num in nums:
        result.append(num ** 2)
    result.sort()
    return result
nums = [-4, -1, 0, 3, 10]

print(sorted_squares(nums))
