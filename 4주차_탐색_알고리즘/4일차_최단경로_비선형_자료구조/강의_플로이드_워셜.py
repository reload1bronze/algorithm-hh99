import sys
from collections import defaultdict
from pprint import pprint

INF = int(1e9)


def floyd_warshall(graph):
    N = len(graph)
    dist = [[INF] * (N + 1) for _ in range(N + 1)]

    for idx in range(1, N + 1):
        dist[idx][idx] = 0

    for start, adjs in graph.items():
        for adj, d in adjs:
            dist[start][adj] = d

    for k in range(1, N + 1):
        for a in range(1, N + 1):
            for b in range(1, N + 1):
                dist[a][b] = min(dist[a][b], dist[a][k] + dist[k][b])

    return dist


with open('testcase_fw.txt') as f:
    sys.stdin = f
    input = sys.stdin.readline

    N = int(input())
    M = int(input())

    graph = defaultdict(list)
    for _ in range(M):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))

    pprint(floyd_warshall(graph))
