# shortening code

def times_two(num):
    return num * 2

nums = []

for num in range(10):
    nums.append(num)
print(nums)

num_list = [num for num in range(10)]
print(num_list)

for i in range(len(nums)):
    num = times_two(nums[i])
    nums[i] = num

print(nums)

times_two_list = list(map(times_two, nums))
print(times_two_list)

times_four_list = list(map(lambda num : num * 4, nums))
print(times_four_list)

nums = [num for num in range(10)]

even_nums = list(filter(lambda num : num%2 == 0, nums))
print(even_nums)

text = "let's split up this text"
print(text.split())

x = 100
if x in even_nums:
    print('x is in even_nums')
else:
    print('x is not in even_nums')

tuples = [(1,2),(3,4),(5,6)]

for a,b in tuples:
    print(a)



