# remove outermost parantheses
# (()())(())->()() + () -> ()()() 
s = "(()())(())"
result = ""
count = 0
for char in  s:
    if char == "(":
        count += 1
        if count > 1:
            result += char
    else:
        count -= 1
        if count > 0:
            result += char
print(result)