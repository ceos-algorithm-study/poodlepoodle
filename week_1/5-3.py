import sys
sys.setrecursionlimit(10 ** 6)

N, M = map(int, sys.stdin.readline().rstrip().split())
frame = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

print(frame)

drcs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def dfs(r, c):
    visited[r][c] = True

    for dr, dc in drcs:
        if r + dr >= 0 and r + dr < N and c + dc >= 0 and c + dc < M and not frame[r + dr][c + dc] and not visited[r + dr][c + dc]:
            dfs(r + dr, c + dc)

cnt = 0
for r in range(N):
    for c in range(M):
        if not frame[r][c] and not visited[r][c]:
            cnt += 1
            dfs(r, c)

print(cnt)