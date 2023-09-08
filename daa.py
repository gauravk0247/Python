import timeit
def fibo(n):
 # Non recursive fibonacci function
 for i in range(2, n + 1):
    fib[i] = fib[i - 1] + fib[i - 2]
 return fib[n]
def fibo_recursive(n):
 # Recursive fibonacci function
 if n == 0:
    return 0
 if n == 1:
    return 1
 fib[n] = fibo_recu(n - 1) + fibo_rec(n - 2)
 return fib[n]
N, RUNS = 20, 1000
print(f"Given N = {N}\n{RUNS} runs")
def callFibo(isRec):
    fib, fib[0], fib[1] =[0] * (N + 1), 0, 1
print("Fibonacci”, "" if isRec else "non", "recursive:",fibo_rec(N) if isRec else fibo(N), "\tTime:",f'{timeit.timeit( fibo_rec(N) if isRec else fibo(N), setup=f"from __main__ import {fibo_rec if isRec else fibo}; N={N}", number=RUNS ):5f}', "O(n)\tSpace: O(", n if else 1, ")", )
callFibo(True)
callFibo(False)