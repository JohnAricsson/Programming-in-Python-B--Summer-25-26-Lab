sample_list = [10, 20, 30, 20, 50]
new_list = []
for item in sample_list:
    if item not in new_list:
        new_list.append(item)

print(new_list)