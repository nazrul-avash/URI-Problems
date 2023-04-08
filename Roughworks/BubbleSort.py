nums = [4444,1,9,41,2]

for i in range(len(nums)):
    largest = nums[0]
    for j in range(len(nums)-i):
        if nums[j] < largest:
            temp = nums[j]
            nums[j] = nums[j - 1]
            nums[j - 1] = temp
        largest = nums[j]


print(nums)