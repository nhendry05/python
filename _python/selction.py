#Nicole Hendry
#Selection Sort

arr = [5, 7, 14, 4, 3, 2, 1, 9, 10]

def sort(arr):
    index = 0
    min = arr[0]
    for x in range (len(arr)):
        min = arr[x]
        for i in range (x, len(arr), 1):
            if min >= arr[i]:
               index = i
               min = arr[i]
        arr[x], arr[index] = arr[index], arr[x]
    return arr
y = sort(arr)
print(y)
