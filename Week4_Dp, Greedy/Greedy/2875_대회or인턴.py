N, M, K = list(map(int,input().split()))
n = N
m = M
team = 0
while True:
    if n >= 2 and m >= 1:
        n -= 2
        m -= 1
        team += 1
    else:
        break
intern = n+m

# 인턴십 수가 모자라다면
while intern < K:
    team -= 1
    intern += 3

print(team)