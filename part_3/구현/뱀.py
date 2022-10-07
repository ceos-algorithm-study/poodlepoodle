# sys.stdin.readline() 사용
import sys
# 뱀의 움직임 및 방향 전환을 위한 deque 사용
from collections import deque

# 보드의 크기 N 입력
N = int(sys.stdin.readline())
# 보드 초기화
board = [[0 for _ in range(N)] for _ in range(N)]
# 뱀 움직임 초기화
snakes = deque([(0, 0)])
board[0][0] = 2

# 사과 갯수 K 및 사과 정보 입력
K = int(sys.stdin.readline())
for _ in range(K):
    r, c = map(int, sys.stdin.readline().rstrip().split())
    board[r - 1][c - 1] = 1

# 방향 전환 횟수 L 및 방향 전환 정보 입력
L = int(sys.stdin.readline())
q = deque()
for _ in range(L):
    sec, rotation = sys.stdin.readline().rstrip().split()
    q.append((int(sec), rotation))

# 방향 설정 (0부터 시계방향으로 동 남 서 북)
direction = 0
moves = ((0, 1), (1, 0), (0, -1), (-1, 0))

# 시뮬레이션 수행
T = 1
while True:

    # 뱀의 다음 머리가 갈 곳 좌표 계산
    head_r, head_c = snakes[-1]
    dr, dc = moves[direction]
    next_r, next_c = head_r + dr, head_c + dc

    # 다음 머리 위치로 이동할 수 없다면 종료
    if next_r < 0 or next_r >= N or next_c < 0 or next_c >= N or board[next_r][next_c] == 2: 
        break

    # 뱀의 꼬리 제외하기 (사과를 먹지 않은 경우는)
    if board[next_r][next_c] == 0:
        prev_r, prev_c = snakes.popleft()
        board[prev_r][prev_c] = 0

    # 뱀의 머리 새로 포함하기)
    snakes.append((next_r, next_c))
    board[next_r][next_c] = 2

    # 방향 전환을 하는 경우
    if q and q[0][0] == T:
        _, rotation = q.popleft()
        if rotation == 'L':
            direction = (direction + 3) % 4
        elif rotation == 'D':
            direction = (direction + 1) % 4

    # 해당 시간이 문제 없이 진행됐을 경우 시간 증가
    T += 1

print(T)
