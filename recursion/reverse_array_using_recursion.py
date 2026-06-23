
def reverse(arr, start, end):
    if start >= end:
        return arr
    arr[start], arr[end] = arr[end], arr[start]
    return reverse(arr, start+1, end-1)


arr = [1, 2, 3, 4, 5]
length = len(arr)
ans = reverse(arr, 1, length-2)
print(ans)