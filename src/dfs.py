import matplotlib.pyplot as plt
time_values = []

def benchmark(func):
    import time

    def wrapper(a, *b):
        start = time.time()
        res = func(a, *b)
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end - start))
        time_values.append(end - start)
        return res
    return wrapper


@benchmark
def dfs_wrap(graph, start, visited=None):
    dfs(graph, start, visited)


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)

    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

print("Graph 1:")
graph_1 = {
  'A': set(['B', 'C']),
  'B': set(['D', 'E']),
  'C': set([]),
  'D': set(['E']),
  'E': set(['F']),
  'F': set([]),
}
dfs_wrap(graph_1, 'A')
print("Graph 2:")
graph_2 = {
  'A': set(['E', 'T', 'B']),
  'E': set(['B']),
  'T': set(['B', 'P']),
  'P': set(['N']),
  'N': set(['T']),
  'B': set(['F', 'C']),
  'F': set(['G', 'C']),
  'G': set([]),
  'C': set(['Z']),
  'Z': set([]),
}
dfs_wrap(graph_2, 'A')
print("Graph 3:")
graph_3 = {
  'A': set(['M', 'E', 'F']),
  'M': set(['L', 'P']),
  'L': set(['N']),
  'N': set(['P']),
  'P': set(['O']),
  'O': set(['B']),
  'B': set(['C']),
  'F': set(['E']),
  'E': set(['C', 'G']),
  'C': set(['D']),
  'G': set(['K']),
  'D': set([]),
  'K': set([]),
}
dfs_wrap(graph_3, 'A')
print("Graph 4:")
graph_4 = {
  'A': set(['B', 'C']),
  'B': set(['E']),
  'C': set(['D']),
  'D': set(['E']),
  'E': set(['F']),
  'F': set(['G']),
  'G': set(['H', 'J', 'I', 'K']),
  'H': set([]),
  'J': set([]),
  'K': set(['L']),
  'L': set(['M']),
  'I': set(['N']),
  'N': set(['O']),
  'O': set(['M']),
  'M': set(['P', 'Q']),
  'P': set([]),
  'Q': set(['R']),
  'R': set([]),
}
dfs_wrap(graph_4, 'A')
print("Graph 5:")
graph_5 = {
  'A': set(['B', 'C', 'D']),
  'B': set(['T']),
  'T': set(['S', 'U', 'Y']),
  'S': set([]),
  'U': set([]),
  'Y': set(['Z']),
  'Z': set([]),
  'C': set(['J', 'K']),
  'J': set(['L']),
  'L': set(['P', 'Q']),
  'P': set([]),
  'Q': set(['R']),
  'R': set([]),
  'K': set(['M']),
  'M': set(['N', 'O']),
  'N': set([]),
  'O': set([]),
  'D': set(['E', 'F']),
  'E': set([]),
  'F': set(['G']),
  'G': set(['H', 'I']),
  'H': set(['I']),
  'I': set([]),
}
dfs_wrap(graph_5, 'A')


plt.figure("DFS Plot")
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