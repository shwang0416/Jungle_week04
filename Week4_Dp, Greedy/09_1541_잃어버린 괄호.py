# [백준] https://www.acmicpc.net/problem/1541 잃어버린 괄호
# 가장 첫번째로 나온 '-' 뒤의 숫자는 그 이후에 어떤 부호가 붙었던지 전부 음수로 계산되게 만들 수 있다.
str = input()
l = len(str)
i = 0

num = ''
numbers = []
cals = []

start = -1
sum_of_minus = -1
sum_of_plus = -1
while i < l:
    if str[i] != '+' and str[i] != '-':
        num += str[i]
        if i == l-1:
            numbers.append(int(num))
    else:
        numbers.append(int(num))
        num = ''
        cals.append(str[i])
    i += 1

for idx in range(len(cals)):
    if cals[idx] == '-':
        start = idx
        break
else:
    print(sum(numbers))
    exit(0)
sum_of_minus = -sum(numbers[start+1:len(numbers)])
sum_of_plus = sum(numbers[0:start+1])
print(sum_of_plus+ sum_of_minus)


