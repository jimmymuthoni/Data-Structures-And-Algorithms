my_array = [64, 34, 25, 12, 22, 11, 90, 5]
n = len(my_array)

for i in range(n):
    min_index = i
    for j in range(i+1, n):
        if my_array[j] < my_array[min_index]:
            min_index = j
    my_array[i], my_array[min_index] = my_array[min_index], my_array[i]

print("sortted array:", my_array)
