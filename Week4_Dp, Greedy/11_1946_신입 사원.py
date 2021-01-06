# [백준] https://www.acmicpc.net/problem/1946 신입 사원

def solve():
    N = int(input())
    cands = []
    ok = []
    for n in range(N):
        a, b = list(map(int,input().split()))
        cands.append([(a,b),abs(a-b)])
    cands.sort(key=lambda x : x[0][0])
    # 샘플 a가 가장 작은 순으로 나열
    # print(cands)
    ok.append(cands[0])
    for i in range(1,N):
        a_sample = ok[-1][0][0]
        b_sample = ok[-1][0][1]
        a_cand = cands[i][0][0]
        b_cand = cands[i][0][1]

        if (a_sample <= a_cand and b_sample >= b_cand) or (a_sample >= a_cand and b_sample <= b_cand):
#       샘플 small보다 후보big이 작으면 또는 샘플 big보다 small이 크면
#       샘플보다 둘 다 작거나 둘 다 큰 것이므로 fail
            ok.append(cands[i])
    print(len(ok))


T = int(input())
for t in range(T):
    solve()