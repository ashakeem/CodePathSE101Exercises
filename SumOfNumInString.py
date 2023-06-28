import string


s = input("input a string with numbers in it: ")

nums = []

sum = 0

for elem in s:
  if elem.isnumeric():
    nums.append(int(elem))

for num in nums:
  sum += num

avg = int(sum / len(nums))

print("The average is: ", avg)
  
    


