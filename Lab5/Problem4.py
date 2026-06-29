nums = [10, 20, 30, 40, 50]
target = int(input("Enter the value to search: "))
found = False

for i in range(len(nums)):
    if nums[i] == target:
        print("Value found at index", i)
        found = True
        break

if not found:
    print("Value not found")