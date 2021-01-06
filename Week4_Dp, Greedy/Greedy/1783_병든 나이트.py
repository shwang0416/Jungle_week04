# [백준] https://www.acmicpc.net/problem/1783 병든 나이트

N, M = list(map(int,input()))
ans = 0
if N < 2 and M < 2:
    ans = 1
elif N < 3 or M < 7:
    # 4번 미만
    ans = N//2+1
    if ans > 4:
        ans == 4

else: