from collections import deque
from queue import Queue
from multiprocessing import Queue as MultQ
time_values = []

def benchmark(func):
  import time

  def wrapper(a, *b):
    start = time.time()
    res = func(a, *b)
    end = time.time()
    print('\n[*] Время выполнения: {} секунд.'.format(end - start))
    time_values.append(end-start)
    return res

  return wrapper


@benchmark
def bfs_list(graph, node):
  visited = []  # List to keep track of visited nodes.
  queue = []
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0)
    print(s, end = " ")

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)


@benchmark
def bfs_deque(graph, node):
  visited = deque() # List to keep track of visited nodes.
  queue = deque()
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.popleft()
    print(s, end = " ")

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)


@benchmark
def bfs_queue(graph, node):
  visited = Queue() # List to keep track of visited nodes.
  queue = Queue()
  visited.put(node)
  queue.put(node)
  while not queue.empty():
    s = queue.get()
    print(s, end = " ")

    for neighbour in graph[s]:
      if neighbour not in iter(visited.queue):
            visited.put(neighbour)
            queue.put(neighbour)


@benchmark
def bfs_mult_queue(graph, node):
  visited = MultQ() # List to keep track of visited nodes.
  queue = MultQ()
  visited.put(node)
  queue.put(node)
  while not queue.empty():
    s = queue.get()
    print(s, end = " ")

    for neighbour in graph[s]:
      if neighbour not in iter(visited.queue):
            visited.put(neighbour)
            queue.put(neighbour)



graph_5 = {
  'A': ['B', 'C', 'D'],
  'B': ['T'],
  'T': ['S', 'U', 'Y'],
  'S': [],
  'U': [],
  'Y': ['Z'],
  'Z': [],
  'C': ['J', 'K'],
  'J': ['L'],
  'L': ['P', 'Q'],
  'P': [],
  'Q': ['R'],
  'R': [],
  'K': ['M'],
  'M': ['N', 'O'],
  'N': [],
  'O': [],
  'D': ['E', 'F'],
  'E': [],
  'F': ['G'],
  'G': ['H', 'I'],
  'H': ['I'],
  'I': [],
} # 23 nodes
bfs_list(graph_5, 'A')
bfs_deque(graph_5, 'A')
bfs_queue(graph_5, 'A')
bfs_mult_queue(graph_5, 'A')