def removeDuplicates(nums):
    # using for loop
    # if len(nums) == 0:
    #     return 0

    # i = 0

    # for j in range(1, len(nums)):
    #     if nums[i] != nums[j]:
    #         i += 1
    #         nums[i] = nums[j]

    # return i + 1

    # using while loop
    n = len(nums)
    left = 0
    right = left+1
    countDupli = 1
    while (right < n):
        if (n < 0):
            return -1

        if (nums[right] == nums[right-1]):
            right += 1
        else:
            nums[left+1] = nums[right]
            left += 1
            countDupli += 1
            right += 1
    return countDupli


nums = [1, 1, 1, 2, 2, 3, 4, 4, 5]
result = removeDuplicates(nums)
print(result)
