# 문제풀이 전략
#   1. S를 구성하는 N개 숫자를 분리 (N <= 20)
#   2. 맨 처음 N을 하나 빼고, 그 다음부터 큐에 남은 숫자들을 하나씩 빼가면서 곱하기 혹은 더하기
#   3. 두 숫자를 연산할 때 두 숫자 중 하나라도 0이나 1인 경우 -> 더하기가 유리하고
#      이를 제외한 모든 나머지 경우 -> 곱하기가 유리함 -> 그리디!

import sys
from collections import deque

q = deque(map(int, list(sys.stdin.readline())))

A = q.popleft()
while q:
    B = q.popleft()
    
    if A == 1 or A == 0 or B == 1 or B == 0:
        A += B
    else:
        A *= B

print(A)