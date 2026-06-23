# fibo 0,1,1,2,3,5,8,...
def fib(n):
    if n <= 1:
        return n

    return fib(n - 1) + fib(n - 2)

print(fib(6))