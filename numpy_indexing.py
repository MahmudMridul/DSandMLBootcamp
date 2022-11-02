import numpy as np
nums = np.arange(0,10)
mat = np.arange(0,9).reshape(3,3)
print(nums[0:3])
print(mat[0:,0:])
print(mat[1:,1:])

nums[0:3] = 100
print(nums)

# copies memory location. doesn't create a new copy
#nums2 = nums[0:3]

nums2 = nums.copy()
nums2[4:7] = 150
print(nums2)

greater_than_five = nums > 5
print(greater_than_five)

print(nums[greater_than_five])

print(nums[nums%2 == 1])