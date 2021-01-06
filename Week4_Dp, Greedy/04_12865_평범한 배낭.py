# [백준] https://www.acmicpc.net/problem/12865 평범한 배낭

import sys
N, K = list(map(int,sys.stdin.readline().split()))

weights = [0]
values = [0]
napsack = [[0 for _ in range(K+1)] for _ in range(N+1)]      # 0부터 K까지의 무게 * 아이템 개수만큼
have = [[[] for _ in range(K+1)] for _ in range(N+1)]

for i in range(N):
    w, v = list(map(int,sys.stdin.readline().split()))
    weights.append(w)
    values.append(v)
for i in range(N+1):
    for j in range(K+1):
        if weights[i] > j:        # 현재 물건의 무게보다 j의 무게가 작으면
            napsack[i][j] = napsack[i-1][j]
        else:                       # i가 아니라 i-1로 하는 이유?? 물건 중복을 방지하기 위해서
                                    # (현재 라인에서 뽑으면 이미 해당 물건이 들어온 상태일 가능성이 있기 때문)
            napsack[i][j] = max(napsack[i-1][j-weights[i]] + values[i], napsack[i-1][j])
print(napsack[-1][-1])

