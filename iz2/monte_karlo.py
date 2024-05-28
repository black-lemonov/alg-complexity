import random
from itertools import combinations

def generate_random_graph(n, p):
    # Создаем пустой граф с n узлами
    graph = {i: set() for i in range(n)}
    # Проходим по всем паре узлов и добавляем ребро с вероятностью p
    for i in range(n):
        for j in range(i+1, n):
            if random.random() < p:
                graph[i].add(j)
                graph[j].add(i)
    return graph

def is_subgraph_isomorphic(g1, g2):
    # Если размеры графов не совпадают, то они не могут быть изоморфными
    if len(g1) != len(g2):
        return False
    # Проходим по всем возможным взаимно однозначным отображениям узлов g1 на узлы g2
    for mapping in combinations(g1, len(g2)):
        # Проверяем, что отображение сохраняет смежность узлов
        if all(n2 in g2[n] for n, n2 in zip(mapping, g2)):
            # Если отображение сохраняет смежность узлов, то графы изоморфны
            return True
    # Если не найдено подходящее отображение, то графы не изоморфны
    return False

def monte_carlo_max_isomorphic_subgraphs(g1, g2, num_trials=1000):
    # Инициализируем переменную, хранящую максимальное количество найденных изоморфных подграфов
    max_num_subgraphs = 0
    # Преобразуем граф g1 в список узлов
    nodes = list(g1.keys())
    # Проходим num_trials раз и генерируем случайный подграф g1
    for _ in range(num_trials):
        # Выбираем случайную подмножество узлов из g1
        selected_nodes = random.sample(nodes, len(g2))
        # Создаем подграф g1, состоящий только из выбранных узлов и их смежных узлов
        subgraph = {node: set(g1[node] & set(selected_nodes)) for node in selected_nodes}
        # Проверяем, что подграф содержит только узлы, присутствующие в g2
        if not set(subgraph.keys()) - set(g2.keys()):
            # Если подграф изоморфен графу g2, то обновляем максимальное количество найденных изоморфных подграфов
            if is_subgraph_isomorphic(subgraph, g2):
                max_num_subgraphs = max(max_num_subgraphs, len(selected_nodes))
    # Возвращаем максимальное количество найденных изоморфных подграфов
    return max_num_subgraphs

# Создаем два случайных графа g1 и g2
g1 = generate_random_graph(10, 0.5)
g2 = generate_random_graph(5, 0.5)

# Находим максимальное количество изоморфных подграфов
max_num_subgraphs = monte_carlo_max_isomorphic_subgraphs(g1, g2)

# Выводим результат
print(f"Максимальное количество изоморфных подграфов: {max_num_subgraphs}")
print(g1)
print(g2)
