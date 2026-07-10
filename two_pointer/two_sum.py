# que is given sorted or non sorted and if we can return on num not indexes then we use two pointer approch
# two sum

# flowchart
# sorting if unsorted array, pairs return krne h nums jinka sum, jo target ke equal honge

# 1 sorting

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    left = merge_sort(left_arr)
    right = merge_sort(right_arr)
    return merge_array(left, right)


def merge_array(left, right):
    i = j = 0
    n = len(left)
    m = len(right)
    result = []
    while i < n and j < m:
        if (left[i] <= right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


# arr = [3, 1, 2, 4, 1, 5, 2, 6, 4]
print("hellow soring")

# print(merge_sort(arr))


def Two_sum(arr, target):
    sortArr = merge_sort(arr)
    i = 0
    j = len(sortArr) - 1

    while i < j:
        sum = sortArr[i]+sortArr[j]

        if (sum == target):
            return sortArr[i], sortArr[j]
        elif sum < target:
            i +=1
        else:
            j -=1
    return None
arr = [3, 1, 2, 4, 1, 5, 2, 6, 4]

print(Two_sum(arr,7))