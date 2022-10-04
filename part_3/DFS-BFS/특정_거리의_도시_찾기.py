# 문제풀이 전략
#   1. 어떤 도시 X로부터 출발하여 도달할 수 있는... -> X부터 완전탐색 시작
#   2. "최단 거리가 정확히 K인" -> DFS나 BFS의 레벨이 K인 경우만 뽑아내기
#   3. 최단 거리 문제 -> visited에 최단 거리를 갱신해 가며
#       더 빨리 도달할 수 있는 경우는 visited를 갱신하고 탐색 이어서 진행
#   4. DFS, BFS 어떤 방식으로든 가능하나 이번에는 DFS로 함

# sys.stdin.readline() 사용
import sys
# python 재귀함수 호출 제한 10^5 설정
sys.setrecursionlimit(10**5)

# 도시 갯수 N, 경로 갯수 M, 주어진 최단 거리 K, 시작 도시 X 입력
N, M, K, X = map(int, sys.stdin.readline().rstrip().split())

# 단방향 그래프이므로 딕셔너리를 사용한 인접 리스트로 구성
routes = dict()
for _ in range(M):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    if A in routes.keys():
        routes[A].append(B)
    else:
        routes[A] = [B]

# 방문 기록 체크를 위한 visited 배열을 충분히 큰 수로 초기화
visited = [300001 for _ in range(N + 1)]

# dfs를 위한 함수 선언
def dfs(current, length):
    # 방문 기록 남기기
    visited[current] = length

    # dfs 레벨이 K보다 커지면 탐색 끊어내기
    if length > K:
        return

    if current in routes.keys():
        # 현재 노드 기준 인접한 노드들 중에서
        for neighbor in routes[current]:
            # 아직 방문하지 않았거나 이전보다 최단 거리로 방문할 수 있는 경우
            if length + 1 < visited[neighbor]:
                # dfs 진행
                dfs(neighbor, length + 1)

# 시작점 방문 체크하고 dfs 수행 시작
visited[X] = 0
dfs(X, 0)

# 방문 기록 중에서 최단거리가 K인 도시들만 필터링
answer = [i for i in range(len(visited)) if visited[i] == K]
if len(answer) == 0:
    print(-1)
else:
    for ans in answer:
        print(ans)
    