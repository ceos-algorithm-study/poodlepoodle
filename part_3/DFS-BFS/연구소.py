# 초기 접근
#   1. BFS로 바이러스가 퍼지는 양상을 그려 본 다음에 가장 많이 거치는 칸 혹은
#       가장 먼저 거치는 칸을 기준으로 우선순위 큐 해서 뽑기??

# 문제풀이 전략
#   1. 연구소 전체에 바이러스가 퍼지는 탐색을 한번 수행 -> O(NM) -> O(10^2)
#   2. 연구소 전체 빈칸 중 벽을 세개 세우는 경우 -> O(10^3)
#   3. 벽을 경우에 따라 전부 세워보더라도 문제에서 요구하는 시간(2초) 내에 충분히 들어올 수 있음
#       -> N과 M의 최댓값이 8로 작기 때문에 가능
#   4. 이런 전략으로 가면 좋은 점 -> bfs로 바이러스가 퍼질 때 각 칸에 최소로 도달하는 것을 고려하지 않고
#       그냥 퍼지는 순간 땡이기 때문에 바로 탐색을 끊어낼 수 있음

# sys.stdin.readline() 사용
import sys
# bfs를 위한 collections.deque 사용
from collections import deque
# 세울 수 있는 벽의 가짓수를 계산하기 위해 itertools.permutations 사용
from itertools import permutations

# 연구소의 세로 길이 N, 가로 길이 M 입력
N, M = map(int, sys.stdin.readline().rstrip().split())
# 바이러스들의 위치 및 빈칸들의 위치를 저장하기 위한 배열 초기화
viruses = []
emptys = []
# 연구소의 원래 지도 정보 입력
original_map = [[1 for _ in range(M + 2)] for _ in range(N + 2)]

# 입력받은 지도 정보에 대해서
for i in range(N):
    line = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(M):
        original_map[i + 1][j + 1] = line[j]
        # 바이러스들의 위치 및
        if line[j] == 2:
            viruses.append([i + 1, j + 1])
        # 빈칸들의 위치를 저장
        elif line[j] == 0:
            emptys.append([i + 1, j + 1])

# 상하좌우 계산을 위한 Offset 입력
directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

# 최댓값 기록 변수 초기화
max_area = -1

# 빈칸들 중에서 세 군데 골라 벽을 세우는 모든 경우의 수
for walls in permutations(emptys, 3):
    # 원래 지도 정보 복사
    maps = [[1 for _ in range(M + 2)] for _ in range(N + 2)]
    for i in range(N):
        for j in range(M):
            maps[i + 1][j + 1] = original_map[i + 1][j + 1]

    # 벽 3개 세우기
    for wall_i, wall_j in walls:
        maps[wall_i][wall_j] = 1

    # 바이러스가 퍼져나가는 모습을 bfs로 시뮬레이션하기 위한 큐 초기화
    q = deque()
    # 바이러스들의 시작 위치 세팅
    for virus_i, virus_j in viruses:
        maps[virus_i][virus_j] = 2
        q.append((virus_i, virus_j))

    # 큐가 비어있지 않을 동안 bfs 수행
    while q:
        # 바이러스의 행 위치 r, 열 위치 c 입력
        r, c = q.popleft()

        # 현재 칸 기준으로 이동할 수 있는 상하좌우 방향에 대해서
        for dr, dc in directions:
            # 해당 칸이 빈 칸이면서 아직 방문하지 않은 경우
            if maps[r + dr][c + dc] == 0:
                # 해당 칸으로의 bfs 수행
                maps[r + dr][c + dc] = 2
                q.append((r + dr, c + dc))

    # 안전 구역의 크기를 구해서
    safe_area = sum([row.count(0) for row in maps])
    # 최댓값 비교 후 갱신
    if safe_area > max_area:
        max_area = max(max_area, safe_area)

# 최대 안전구역 출력
print(max_area)
