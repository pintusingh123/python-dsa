# find the largest odd number in a string
def largest_odd_number(s):
    n = len(s)
    for i in range(n-1, -1, -1):
        if int(s[i]) % 2 == 1:
            return s[:i+1]
    return ""