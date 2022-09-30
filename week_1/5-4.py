import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())
maze = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]
visited = [[40001 for _ in range(M)] for _ in range(N)]

drcs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

q = deque([])
q.append([0, 0, 1])
visited[0][0] = 1
answer = 1

found = False
while len(q) != 0:
    r, c, level = q.popleft()

    if r == N - 1 and c == M - 1:
        answer = level
        break

    for dr, dc in drcs:
        if r + dr >= 0 and r + dr < N and c + dc >= 0 and c + dc < M:
            if visited[r + dr][c + dc] > level + 1:
                visited[r + dr][c + dc] = level + 1
                q.append([r + dr, c + dc, level + 1])

print(answer)
