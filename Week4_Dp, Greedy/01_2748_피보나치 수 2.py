# [백준] https://www.acmicpc.net/problem/2748 피보나치 수 2
import sys
N = int(input())
arr = [-1 for _ in range(N+1)]
arr[0] = 0
arr[1] = 1


def fibonacci(n):
    if n == 0 or n == 1:
        return arr[n]
    if arr[n] > 0 :
        return arr[n]
    else:
        arr[n] = fibonacci(n-1) + fibonacci(n-2)
        return arr[n]

print(fibonacci(N))