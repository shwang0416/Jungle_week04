# [백준] https://www.acmicpc.net/problem/1904 01타일
# [참고] https://blog.naver.com/occidere/220787441430
# 왜 15746으로 미리 나눠서 구해도 숫자가 동일할까??
# => '나머지 정리'

N = int(input())
# N일 때 만들 수 있는 모든 경우의 가짓 수는 N-2와 N-1일 때 만들 수 있는 모든 가짓 수의 총합


def solve(N):
    a = [0 for _ in range(N + 1)]
    ans = 1
    if N == 1:
        print(ans)
        exit(0)
    elif N >= 2:

        a[1] = 1
        a[2] = 2
        n = 3
        while n <= N and a[n] == 0:
            a[n] = a[n - 1] + a[n - 2]
            a[n] %= 15746
            n += 1
        print(a[n - 1])
        # print(a)


solve(N)



