# 풀이 전략
#   1. 여러 테스트 케이스를 직접 손으로 건드려 보면
#   2. "0이 모여있는 부분 집합" 과 "1이 모여 있는 부분 집합" 의 수 중에서
#   3. 무조건 작은 수 만큼이 최소 횟수라는 것을 알 수 있음

import sys
from collections import deque

string = deque(sys.stdin.readline().rstrip())

zeros = 0
ones = 0

prev = string.popleft()
if prev == '0':
    zeros += 1
else:
    ones += 1

while string:
    current = string.popleft()

    if current == prev:
        continue

    if current == '0':
        zeros += 1
    else:
        ones += 1

    prev = current

print(zeros if zeros < ones else ones)
