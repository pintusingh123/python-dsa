# write program to store num frequency on dict

num = [1,2,3,3,4,2,1,6,7,8,6,8]

# using hashmap and get()


hash_map={}
for i in range(0, len(num)):
  hash_map[num[i]] = hash_map.get(num[i],0) + 1
print(hash_map)



# free = {}
# method 1
# for n in num:
#   if n in free:
#     free[n] += 1
#   else:
#     free[n] = 1
# method 2 
# for i in range(0, len(num)):
#   if num[i] in free:
#     free[num[i]] += 1
#   else:
#     free[num[i]] = 1

# print(free)

