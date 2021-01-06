# [백준] https://www.acmicpc.net/problem/9251 LCS
# [참고] https://www.youtube.com/watch?v=ASoaQq66foQ 유튜브 강의
import sys
# 2차원 리스트를 만들어 각각의 글자가 매치되는지 확인한다
str1 = sys.stdin.readline().strip()
str2 = sys.stdin.readline().strip()
str1 = list(str1)
str2 = list(str2)
str1.insert(0,'')
str2.insert(0,'')
check = [[-1 for _ in range(len(str2))] for _ in range(len(str1))]

for i in range(len(str1)):
    for j in range(len(str2)):
        if str1[i] == '' or str2[j] == '':
            check[i][j] = 0
        elif str1[i] == str2[j]:
            check[i][j] = 1 + check[i-1][j-1]
        else:
            check[i][j] = max(check[i-1][j], check[i][j-1])
print(check[-1][-1])
