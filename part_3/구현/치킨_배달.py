# 풀이 전략
#   1. 도시의 치킨집을 고르는 조합의 수 : M이 최대 13이므로 13!
#   2. 특정 집 기준으로 치킨 거리를 구하는 시간 : O(M)
#   3. 모든 집의 치킨 거리를 구하는 시간 : O(2N * M)
#   * 결론적으로 N과 M의 최댓값이 매우 크지 않기 때문에 완전탐색(Bruteforcing)으로 풀이 가능

# sys.stdin.readline() 사용
import sys
# 치킨 집을 고르는 경우의 수를 위해 itertools.combinations 사용
from itertools import combinations

# 도시의 가로 및 세로 크기 N 및 치킨집 조합의 수 M 입력
N, M = map(int, sys.stdin.readline().rstrip().split())
# 도시 정보 입력
city = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
# 도시의 집 정보와 치킨 정보를 따로 리스트에 저장해 놓기
houses = []
total_chicks = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            houses.append((i, j))
        elif city[i][j] == 2:
            total_chicks.append((i, j))

# 도시의 최소 치킨 거리 비교 변수 충분히 큰 수로 초기화
min_len_chick = 30000
# 모든 치킨집을 고르는 경우의 수마다
for chicks in combinations(total_chicks, M):
    # 도시의 치킨 거리 저장 변수 초기화
    len_chick = 0
    # 중간에 이미 최소 치킨 거리보다 커지는 경우 완전탐색을 끊어내기 위함
    backtracking = False
    
    # 모든 집마다
    for house in houses:
        # 각 집에서 가장 가까운 치킨 거리 비교를 위한 변수 충분히 큰 수로 초기화
        nearest_chick = 30000
        for chick in chicks:
            nearest_chick = min(nearest_chick, abs(chick[0] - house[0]) + abs(chick[1] - house[1]))
        len_chick += nearest_chick

        # 계산 중인 치킨집 조합의 치킨 거리가 최소 치킨 거리보다 이미 커진 경우
        if len_chick >= min_len_chick:
            # 백트래킹 플래그 설정
            backtracking = True
            break

    # 효율적인 완전탐색을 위한 백트래킹
    if backtracking:
        continue
    
    # 해당 치킨집의 조합이 최소 치킨 거리를 산출하는지 확인 후 최솟값 갱신
    min_len_chick = min(min_len_chick, len_chick)

# 정답 출력
print(min_len_chick)
