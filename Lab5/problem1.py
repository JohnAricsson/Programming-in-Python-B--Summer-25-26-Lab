string = "American International University"

words = string.split()
res = []

for word in words:
    res.append(word[::-1])

result = " ".join(res)

print("Original String:", string)
print("Reversed Words:", result)