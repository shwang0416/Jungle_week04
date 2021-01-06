# [백준] https://www.acmicpc.net/problem/1700 멀티탭 스케줄링
import sys
from collections import deque

sys.stdin = open('1700.txt')

N, K = list(map(int,sys.stdin.readline().split()))
waiting_line = deque(sys.stdin.readline().split())
use_cnt = [0 for _ in range(K+1)]
multitab = [-1 for _ in range(N)]
plug_out = 0

for i in range(K):
    idx = int(waiting_line[i])
    use_cnt[idx] += 1
if N >= K:
    print(0)
    exit(0)
else:
    for i in range(N):
        multitab[i] = waiting_line.popleft()
        use_cnt[int(multitab[i])] -= 1
    w = len(waiting_line)
    for _ in range(w):
        c = waiting_line.popleft()
        if c in multitab:           # 새로 쓸 전자기기가 이미 꽂혀있다면
            use_cnt[int(c)] -= 1
            continue
        last = 0
        for m in multitab:
            for i in range(len(waiting_line)-1,-1,-1):
                if waiting_line[i] == m:
                    last = i if i > last else last      # 사용중인 멀티탭에서 후에 가장 뒤에서 쓸 전자기기의 인덱스
                    print(m, last)
                    break
        print()
        multitab[multitab.index(waiting_line[last])] = c
        plug_out += 1
        use_cnt[int(c)] -= 1
    print(plug_out)







