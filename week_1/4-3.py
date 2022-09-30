import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
r, c, direction = map(int, sys.stdin.readline().rstrip().split())
board = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

drcs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

while True:
    # 1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향(반시계 방향으로 90도 회전한 방향)부터 차례대로 갈 곳을 정한다.
    found = False
    for i in range(4):
        dr, dc = drcs[(direction + 4 - i) % 4]

        # 2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면,
        if not visited[r + dr][c + dc] and not board[r + dr][c + dc]:
            # 왼쪽 방향으로 회전한 다음 왼쪽으로 한 칸을 전진한다.
            direction = (direction + 4 - i) % 4
            r, c = r + dr, c + dc
            visited[r][c] = True
            found = True
        
        # 왼쪽 방향에 가보지 않은 칸이 없다면, 왼쪽 방향으로 회전만 수행하고 1단계로 돌아간다.
        if found: break

    if found: continue
    
    # 3. 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우에는,
    # 바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로 돌아간다.
    dr, dc = drcs[(direction + 6) % 4]

    if not board[r + dr][c + dc]:
        r, c = r + dr, c + dc
        found = True

    if found: continue

    # 단, 이때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다.

    break

answer = sum(line.count(True) for line in visited)
print(answer)
