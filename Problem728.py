# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
# such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.

def fib (n: int) -> int:
    fib0 = 0
    fib1 = 1
    
    for i in range(n - 1):
        fibRes = fib0 + fib1
        fib0 = fib1
        fib1 = fibRes
    return fibRes

if __name__ == "__main__":
    print(fib(9))
