# 소요 시간 : 13분
# 풀이 전략
#   1. 동전의 갯수 - 최대 10^3
#   2. 동전들로 어떤 금액이 조합 가능한지의 여부는, 작은 동전부터 살펴보는 것이 좋으므로 오름차순으로 정렬
#   3. 동전을 작은 순서대로 하나씩 조합 재료로 사용해 보면,
#       새로 추가된 동전이 지금까지 시도했던 최대 금액보다 작거나 같아야 하며,
#       그렇지 않은 시점의 최대 금액이 정답
# 그리디 포인트 : 새로 추가된 동전을 이용해 만들 수 있는 최대 금액을 계산할 때 이전까지 추가된 동전들의 정보를 이용

import sys

N = int(sys.stdin.readline())
coins = list(map(int, sys.stdin.readline().rstrip().split()))
coins.sort()

answer = 1
for coin in coins:
    if coin <= answer:
        answer += coin
    else:
        break

print(answer)

