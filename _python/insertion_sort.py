#Nicole Hendry
#Insertion Sort

arr = [5, 7, 14, 4, 3, 2, 1, 9, 10]

def insertion_sort(arr):
    for i in range (1, len(arr), 1):
        for x in range (i-1, -1, -1):
            var_i = arr[i]
            var_x = arr[x]
            if arr[i] < arr[x]:
                arr[i], arr[x] = arr[x], arr[i]
                i = i-1
    return arr
y = insertion_sort(arr)
print(y)



