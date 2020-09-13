some_list = [1,2,3,4,5,6]

some_list.append(10)

print("Slice", some_list[0])
print("Slice", some_list[1])
print("Slice", some_list[2])
print("Slice", some_list[3])
print("Slice", some_list[4])

for each in range(len(some_list)):
    print("Index", each)

for each in range(len(some_list)):
    print("Data", some_list[each])

