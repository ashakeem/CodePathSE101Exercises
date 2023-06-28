

s = input("input a string with numbers in it: ")
max_consec = 0
current_consec = 0
nums = []
sum = 0

for elem in s:
  if elem.isnumeric():
    nums.append(int(elem))
    current_consec += 1
  else:
    current_consec = 0

  if current_consec > max_consec:
    max_consec = current_consec
  
for num in nums:
  sum += num

 
avg = int(sum / len(nums))

print("The average is: ", avg)
print("Max occourence of consecutive number is: ", max_consec)



