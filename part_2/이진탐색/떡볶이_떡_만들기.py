import sys

def input(): return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
dducks = list(map(int, input().split()))

# N의 최댓값 10^6, M의 최댓값 2*10^9
# 순차적으로 따지는 경우 모든 M마다 N을 테스트해야 함
# 이 경우는 M을 1씩 줄여 보면서 테스트하는 대신 이분 탐색으로 찾아가도록 할 수 있음

max_dducks = max(dducks)
start = 1
end = max_dducks
answer = -1

while start <= end:
    middle = (start + end) // 2

    # 절단기의 높이
    height = max_dducks - middle

    # 해당 절단기의 높이로 잘라낼 수 있는 떡의 총 길이
    _sum = 0
    for dduck in dducks:
        _sum += (dduck - height) if dduck - height > 0 else 0
    
    if _sum == M:
        answer = height
        break
    elif _sum > M:
        answer = height
        end = middle - 1
    else:
        start = middle + 1

print(answer)
