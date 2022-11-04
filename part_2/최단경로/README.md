# 최단 경로 알고리즘 - 이코테 요약

## 핵심

**한 지점에서 다른 특정 지점까지의 가장 짧은 거리를 구하는 알고리즘**  
= "길 찾기 문제"

## 최단 거리 알고리즘의 종류

- **다익스트라 (Dijkstra) 알고리즘**
- **플로이드-워셜 (Floyd-Warshall) 알고리즘**
- 벨만-포드 (Bellman-Ford) 알고리즘

## 다익스트라 (Dijkstra) 알고리즘

**간선의 가중치가 음수가 아니라는 가정 하에 사용 가능한 대표적인 최단 거리 알고리즘**

> 알고리즘이 수행되는 순서

1. 출발 노드와 도착 노드를 설정한다.
2. "최단 거리 테이블"을 초기화한다.
3. 현재 위치한 노드의 인접 노드 중 방문하지 않은 노드를 구별하고, 방문하지 않은 노드 중 거리가 가장 짧은 노드를 선택한다. 그 노드를 방문 처리한다.
4. 해당 노드를 거쳐 다른 노드로 넘어가는 간선 비용(가중치)을 계산해 "최단 거리 테이블"을 업데이트한다.
5. 아직 방문하지 않은 노드가 남아있는 동안 3 ~ 4의 과정을 반복한다.

"최단 거리 테이블" 은 특정 시작점으로부터 각 노드에 도달하는 최단 거리를 매번 갱신해 값을 저장하며, 맨 처음에는 충분히 큰 수 `(10^9)` 로 초기화한다.

> 그림으로 확인하기

![](https://i.imgur.com/xmSTwmo.png)

![](https://i.imgur.com/PqEubsG.png)

![](https://i.imgur.com/UvwvTEg.png)

![](https://i.imgur.com/Z5mkKmS.png)

![](https://i.imgur.com/tWv7jcY.png)

![](https://i.imgur.com/8wDAQGU.png)

![](https://i.imgur.com/ki9XkdO.png)

![](https://i.imgur.com/AHtflyf.png)

_이미지 출처 : https://chanhuiseok.github.io/posts/algo-47/_

> 코드로 구현하기

```python
import sys
def input(): return sys.stdin.readline().rstrip()
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n + 1)]
# 방문한 적이 있는지 체크하는 목적의 리스트를 만들기
visited = [False] * (n + 1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0 # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n - 1개의 노드에 대해 반복
    for i in range(n - 1): # 정점의 갯수인 최대 V번만큼 연산
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]: # 연결된 다른 정점의 갯수인 최대 V-1번만큼 연산
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

# 다익스트라 알고리즘을 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])
```

> 시간 복잡도

**O(V^2)** : V는 정점의 갯수

그래프 상의 정점을 모두 탐색하는 데 V번,
각 정점마다 연결된 노드를 모두 탐색하는 데 V번이므로 O(V^2)가 소요됨

전체 노드의 갯수가 5000개 이하인 경우 무난하게 위 알고리즘으로 풀 수 있다고 가정

> 개선된 다익스트라 알고리즘

정점마다 연결된 노드를 모두 탐색하는 데 걸리는 V번의 연산을
**우선순위 큐**를 이용해 효율적으로 계산하도록 수정함

일반 리스트

- 삽입 시간 : O(1)
- 추출 시간 : O(N)

힙 (Heap)

- 삽입 시간 : **O(logN)**
- 추출 시간 : **O(logN)**

추출되는 값의 성질에 따라 **최소 힙** 또는 **최대 힙**으로 구분

> 개선된 알고리즘 수행 순서

1. 출발 노드와 도착 노드를 설정한다.
2. "최단 거리 테이블"을 초기화한다. **또한, 시작 노드를 우선순위 큐에 넣는다.**
3. 큐의 요소를 하나 추출한다.
4. 큐에서 꺼낸 노드의 최단 거리가 "최단 거리 테이블"의 최단 거리보다 작은 경우만 다음으로 이어서 진행한다. 아닌 경우 다시 3으로 반복한다.
5. 최단 거리 테이블의 값을 새롭게 갱신한다.
6. 현재 위치한 노드의 인접 노드 및 계산된 최단 거리를 우선순위 큐에 전부 넣는다.
7. 우선순위 큐가 비어 있지 않다면 3부터 다시 반복한다.

> 개선된 시간 복잡도

**O(ElogV)** : V는 정점의 갯수, E는 간선의 갯수

그래프 상의 간선을 모두 한 번씩 우선순위 큐에 삽입하고,
이 간선들이 모두 우선순위 큐에서 제거되었을 때 알고리즘이 종료된다.  
힙의 한 요소를 추출하는 데는 O(logN)이 소요되는데 이를 모든 요소 N개만큼
반복하므로 O(NlogN), 삽입-삭제 총 2번씩이므로 O(2NlogN)

![image](https://user-images.githubusercontent.com/6462456/199970006-ef89193f-8639-47b3-b1d2-6a504b832eec.png)  
_간선의 갯수 E는 정점의 개수 V^2보다 항상 작거나 같다_

```plaintext
O(2ElogE)
>= O(2ElogV^2)
= O(4ElogV)
= O(ElogV)
```

> 파이썬에서의 우선순위 큐 사용 : PriorityQueue / heapq

- PriorityQueue

```python
from queue import PriorityQueue

q = PriorityQueue()

# 요소 삽입
que.put(4)
que.put(1)
que.put(7)
que.put(3)

# 요소 삭제
print(que.get()) # 1
print(que.get()) # 3
print(que.get()) # 4
print(que.get()) # 7
```

- collections.heapq

```python
import heapq

heap = []

# 요소 삽입
heapq.heappush(heap, 4)
heapq.heappush(heap, 1)
heapq.heappush(heap, 7)
heapq.heappush(heap, 3)
print(heap) # [1, 3, 7, 4]

# 요소 삭제
print(heappop(heap)) # 1
print(heap) # [3, 4, 7]

# 최솟값을 삭제하지 않고 그냥 접근하기
print(heap[0]) # 1

# 기존 리스트를 힙으로 변환
q = [4, 1, 7, 3, 8, 5]
heapq.heapify(q)
print(q) # [1, 3, 5, 4, 8, 7]

# 최대 힙 방식으로 사용하기
for num in nums:
  heappush(heap, (-num, num))  # (우선 순위, 값)
```

대부분의 경우에는 PriorityQueue보다 속도가 빠른 **heapq 사용을 권장함**

## 벨만-포드 (Bellman-Ford) 알고리즘

**2차원 리스트 형식의 최단 거리 테이블을 가지고 다이나믹 프로그래밍 방식으로 최단 거리를 구하는 알고리즘**

```python
# 메인 아이디어
D[a][b] = min(D[a][b], D[a][k] + D[k][b])

# 구현
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            adj[a][b] = min(adj[a][b], adj[a][k] + adj[k][b])
```

- 아직 정확히 이해하지 못했음...

## 문제 풀이

> 백준 11404번 - 플로이드

![image](https://user-images.githubusercontent.com/6462456/199975166-414b3554-b5c1-45d9-b5cb-cc7d31b9c543.png)

[http://acmicpc.net/problem/11404](http://acmicpc.net/problem/11404)

문제에서 **모든 출발 - 도착 정점 쌍에 대해 최단 거리**를 구하라고 요구했으므로 플로이드-워셜 알고리즘을 이용한 풀이가 적합함

```python
import sys

def input(): return sys.stdin.readline().rstrip()
INF = int(1e9)

n = int(input()) # 도시의 개수 n
m = int(input()) # 버스의 개수 m
bus = [list(map(int, input().split())) for _ in range(m)] # 도시 사이를 있는 버스 비용 list

# 도시간 버스 비용을 담을 2차원 list. 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에게 가는 비용 = 0 으로 초기화
for i in range(1, n + 1):
	graph[i][i] = 0

# 모든 버스 연결 정보를 저장
# i[0]: 출발 도시, i[1]: 도착 도시, i[2]: 버스 비용
# 도시간 버스가 중복되는 경우, 더 적은 비용으로 저장
for start, end, cost in bus:
	# graph[i[0]][i[1]]: 기존에 graph에 저장된 비용, i[2]: 방금 꺼낸 비용
    # 방금 꺼낸 비용이 더 저렴할 경우 새로운 값으로 갱신
    graph[start][end] = min(graph[start][end], cost)

# 플로이드 워셜 알고리즘 수행
# 점화식: D_ab = min(D_ab, D_ak + D_kb)
for k in range(1, n + 1):
	for a in range(1, n + 1):
		for b in range(1, n + 1):
			# a에서 b로 가는 비용
			# =a에서 b로 가는 비용과 a에서 k를 거쳐 b로 가는 비용 중 적은 비용
			graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n + 1):
	for b in range(1, n + 1):
		# a에서 b로 갈 수 없는 경우, 0을 출력해야함
		if graph[a][b] == INF:
			graph[a][b] = 0

for i in range(1, n + 1):
	print(*graph[i][1:])
```

> 백준 1753번 - 최단 거리

![image](https://user-images.githubusercontent.com/6462456/199975982-435e816e-7ffe-4512-bbc9-9d489d775617.png)

[http://acmicpc.net/problem/1753](http://acmicpc.net/problem/1753)

대표적인 다익스트라 문제, heqpq를 이용한 풀이

```python
import sys
import heapq

def input(): return sys.stdin.readline().rstrip()
INF = int(1e9)

V, E = map(int, input().split())

# 시작점 K
K = int(input())

# 최단 거리 테이블 초기화
table = [INF] * (V + 1)

# 우선순위 큐 초기화
heap = []
graph = [[] for _ in range(V + 1)]

def dijkstra(start):
    # 최단 거리 테이블에서 시작 정점에 해당하는 가중치는 0으로 초기화
    table[start] = 0
    heapq.heappush(heap,(0, start))

    # 우선순위 큐가 비어있지 않을 동안 반복
    while heap:
        cost, now = heapq.heappop(heap)

        # 현재 테이블과 비교하여 불필요한(더 가중치가 큰) 튜플이면 무시.
        if table[now] < cost:
            continue

        for w, next_node in graph[now]:
            # 현재 정점 까지의 가중치 cost + 현재 정점에서 다음 정점(next_node)까지의 가중치 W
            # = 다음 노드까지의 가중치 (new_cost)
            new_cost = w + cost
            # 다음 노드까지의 가중치 (new_cost)가 현재 기록된 값 보다 작으면 조건 성립
            if new_cost < table[next_node]:
                # 계산했던 new_cost를 가중치 테이블에 업데이트
                table[next_node] = new_cost
                # 다음 점 까지의 가증치와 다음 점에 대한 정보를 튜플로 묶어 최소 힙에 삽입
                heapq.heappush(heap,(new_cost,next_node))

# 초기화
for _ in range(E):
    u, v, w = map(int, input().split())
    # (가중치, 목적지 노드) 형태로 저장
    graph[u].append((w, v))

dijkstra(K)
for i in range(1,V+1):
    print("INF" if table[i] == INF else table[i])
```
