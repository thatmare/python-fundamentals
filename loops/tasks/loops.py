# Task1. Create a list that contains elements of integer type, then use the loop to change the type of these elements to a floating type.

nums_list = list(range(0, 11))

for x in nums_list:
    x = float(x)
    print(type(x))
    
# Task2. Print Fibonacci numbers up to the entered number n, using cycles.
   
stop = input('Enter a number:')
nums = list(range(0, int(stop)))

for x in nums:
  if x == 0 or x == 1:
    nums[x] = x
  else:
    nums[x] = nums[x-1] + nums[x-2]

print(nums)

# Task3. Write a script that will calculate the factorial of the entered number without using recursion.

n = input('Enter a number:')

nums = list(range(1, int(n) + 1))

for i in range(len(nums)):
    nums[i] = nums[i] * nums[i-1]

print(nums[len(nums) - 2])