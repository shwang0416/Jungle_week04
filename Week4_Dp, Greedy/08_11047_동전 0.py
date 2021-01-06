# [백준] https://www.acmicpc.net/problem/11047 동전0
import sys
N, K = map(int,input().split())
coin = [int(sys.stdin.readline()) for _ in range(N)]
ans = 0
for i in range(N-1, -1, -1):
    while K >= coin[i]:
        K -= coin[i]
        ans += 1
print(ans)
