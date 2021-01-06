# [백준] https://www.acmicpc.net/problem/1931 회의실배정
import sys

N = int(input())
a = [tuple(map(int,sys.stdin.readline().split())) for _ in range(N)]
ans = []

a.sort()
a.sort(key=lambda x:x[1])
i = 0
ans.append(a[i])
while i < N:
    for j in range(i+1,N):
        if a[i][1] <= a[j][0]:      # i의 끝나는시간보다 j의 시작시간이 같거나 크다면
            ans.append(a[j])
            i = j
    else:
        break
print(len(ans))