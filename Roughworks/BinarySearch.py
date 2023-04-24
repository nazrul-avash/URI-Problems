
def insertPosition(nums,key):
    begin = 0
    end = len(nums)-1
    mid = 0
    while(begin<=end):
        mid = (begin + end)//2
        if nums[mid] == key:
            return mid
        if nums[mid]<key :
            begin = mid+1
        if nums[mid]>key:
            end = mid -1
    return mid+1

def rotationNumber(nums):
    begin = 0
    end = len(nums)-1
    mid = 0
    while(begin<=end):
        mid = (begin + end)//2
        if nums[mid]>nums[-1] and nums[mid]>nums[mid+1]:
            return mid+1
        if nums[mid]<nums[-1]:
            end = mid-1
        if nums[mid]>nums[-1]:
            begin = mid +1
    return mid
def Search(nums,key):
    if len(nums)>1:
        begin = 0
        end = len(nums)-1
        mid = (begin + end) // 2
        while(begin<=mid and end<=len(nums)-1):
            if key == nums[mid]:
                return mid
            if key > nums[mid]:
                begin = mid+1
                mid = (begin + end) // 2
            if key<nums[mid]:
                end = mid - 1
                mid = (begin + end) // 2



numbers = [16,45,67]
print(rotationNumber(numbers))
