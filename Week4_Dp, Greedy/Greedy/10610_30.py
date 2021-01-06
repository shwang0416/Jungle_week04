# [백준] https://www.acmicpc.net/problem/10610 30
N = input()
N = list(N)

l = len(N)
ans = -1
three = 0

if '0' in N:
    for i in range(len(N)):
        three += int(N[i])
    if three % 3 == 0:      # 3의 배수
        N.sort(reverse=True)
        ans = ''.join(N)
print(ans)

