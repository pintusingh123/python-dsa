# given n , m list inside the n ele is 1 <=n & <=10
# and m ale free in n list

n = [1, 2, 3, 2, 3, 6, 6, 10, 8, 9]
m = {11, -2, 3, 4, 5, 6, 7, 10}

hash_list = [0]*11
for num in n:
    hash_list[num] += 1
for num in m:
    if num < 1 or num > 10:
        print("ok")
    else:
        print(hash_list[num], end=" ")
