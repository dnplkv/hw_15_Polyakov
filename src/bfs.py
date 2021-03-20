import matplotlib.pyplot as plt
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
def bfs(graph, node):
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


graph_1 = {
  'A': ['B', 'C'],
  'B': ['D', 'E'],
  'C': [],
  'D': ['E'],
  'E': ['F'],
  'F': [],
} # 6 nodes
print("Graph 1:")
bfs(graph_1, 'A')

graph_2 = {
  'A': ['E', 'T', 'B'],
  'E': ['B'],
  'T': ['B', 'P'],
  'P': ['N'],
  'N': ['T'],
  'B': ['F', 'C'],
  'F': ['G', 'C'],
  'G': [],
  'C': ['Z'],
  'Z': [],
} # 10 nodes
print("Graph 2:")
bfs(graph_2, 'A')

graph_3 = {
  'A': ['M', 'E', 'F'],
  'M': ['L', 'P'],
  'L': ['N'],
  'N': ['P'],
  'P': ['O'],
  'O': ['B'],
  'B': ['C'],
  'F': ['E'],
  'E': ['C', 'G'],
  'C': ['D'],
  'G': ['K'],
  'D': [],
  'K': [],
} # 13 nodes
print("Graph 3:")
bfs(graph_3, 'A')

graph_4 = {
  'A': ['B', 'C'],
  'B': ['E'],
  'C': ['D'],
  'D': ['E'],
  'E': ['F'],
  'F': ['G'],
  'G': ['H', 'J', 'I', 'K'],
  'H': [],
  'J': [],
  'K': ['L'],
  'L': ['M'],
  'I': ['N'],
  'N': ['O'],
  'O': ['M'],
  'M': ['P', 'Q'],
  'P': [],
  'Q': ['R'],
  'R': [],
} # 18 nodes
print("Graph 4:")
bfs(graph_4, 'A')

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
print("Graph 5:")
bfs(graph_5, 'A')


plt.figure("BFS Plot")
plt.title("Зависимость времени выполнения алгоритма от количества вершин")
plt.xlabel("Время выполнения, с*10^(-5)") # ось абсцисс
plt.ylabel("О|V|+|E|") # ось ординат
plt.plot([time_values[0], time_values[1], time_values[2], time_values[3], time_values[4]], [11, 23, 28, 37, 46])
dot1 = plt.scatter(time_values[0], 11, color='pink', s=40, marker='o', label='Первый граф')
dot2 = plt.scatter(time_values[1], 23, color='orange', s=40, marker='o', label='Второй граф')
dot3 = plt.scatter(time_values[2], 28, color='red', s=40, marker='o', label='Третий граф')
dot4 = plt.scatter(time_values[3], 37, color='purple', s=40, marker='o', label='Четвертый граф')
dot5 = plt.scatter(time_values[4], 46, color='black', s=40, marker='o', label='Пятый граф')
plt.legend()
plt.show()