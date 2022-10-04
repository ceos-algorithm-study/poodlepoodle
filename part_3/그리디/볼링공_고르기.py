# 풀이 전략
#   1. 볼링공 무게의 범위가 최대 10으로 작은 편
#   2. 같은 무게의 공이 존재해도 서로 다른 공으로 취급
#   3. 어떤 두 무게의 공을 고르는 경우의 수 * 해당 무게를 가진 공의 개수로 구함

import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
balls = list(map(int, sys.stdin.readline().rstrip().split()))
ball_dict = {}
for ball in balls:
    if ball in ball_dict.keys():
        ball_dict[ball] += 1
    else:
        ball_dict[ball] = 1

answer = 0
for first in [weight for weight in ball_dict.keys() if weight <= M]:
    for second in [weight for weight in ball_dict.keys() if weight <= M]:
        if first != second:
            answer += ball_dict[first] * ball_dict[second]

# (무게가 1인 공의 수 * 무게가 3인 공의 수) 와 (무게가 3인 공의 수 * 무게가 1인 공의 수) 는 중복되므로
# 중복되는 경우를 고려해 2로 나누어 준다.
print(answer // 2)