import sys

def djikstra(graph, start, end):
  inf = sys.maxsize
  dist = {i: {'cost': inf, 'pred': []} for i in graph.keys()}
  dist[start]['cost'] = 0
  visited = set()
  print(dist)

graph = {
  'A': {'B': 2, 'C': 3},
  'B': {'A': 2, 'C': 2, 'D': 4},
  'C': {'A': 3, 'B': 2, 'D': 5, 'E': 3},
  'D': {'B': 4, 'C': 5, 'E': 1, 'F': 3},
  'E': {'C': 3, 'D': 1, 'F': 4},
  'F': {'D': 3, 'E': 4}
}
start, end = ['A', 'F']

djikstra(graph, start, end)