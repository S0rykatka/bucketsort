tab = [0, 0.5, 0.88, 0.7, 0.33, 0.2, 0.15, 1]
Bucket = int(input())
b_range = ((max(tab) - min(tab)) / Bucket)
array = []
for i in range(Bucket):
    buck = []
    array.append(buck)
    print(array)
for a in tab:
    index = int((a - min(tab)) / b_range)
    if a == max(tab):
        index = index - 1
    array[index].append(a)
    print(array)
for buck in array:
    buck.sort()
arrsort = []
for i in array:
    for y in i:
        arrsort.append(y)
print(arrsort)