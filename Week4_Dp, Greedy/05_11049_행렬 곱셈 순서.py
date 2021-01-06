# [백준] https://www.acmicpc.net/problem/11049 행렬 곱셈 순서
import sys
from functools import reduce

N = int(sys.stdin.readline().strip())
a = [list(map(int,sys.stdin.readline().split()))for _ in range(N)]

table = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    table[i][i] = 0
# 같은 배열일 경우 0으로 세팅

def multiply(arr):
    return reduce(lambda x, y: x * y, arr)

s = set()
for i in range(N):
    j = i+1
    s.add(a[i][0])
    s.add(a[i][1])
    s.add(a[j][0])
    s.add(a[j][1])
    result = multiply(s)
    table[i][j] = result
    s.clear()
# print(table)
# 1차 계산 완료 (배열 둘 끼리 짝지은 경우의 수)

for i in range(N):
    j = i+1
    s.add(a[i][0])
    s.add(a[i][1])
    s.add(a[j][0])
    s.add(a[j][1])
    result = multiply(s)
    table[i][j] = result
    s.clear()