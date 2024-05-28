
# Определяем функцию для поиска изоморфных подграфов
def subgraph_isomorphism(g1, g2):
    # Внутренняя функция для рекурсивного поиска изоморфных подграфов
    def _subgraph_isomorphism(g1, g2, nodes_g1, nodes_g2):
    # Если nodes_g2 пуст, то мы нашли изоморфный подграф
            if not nodes_g2:
                return [[]]
            # Если nodes_g1 пуст, то мы не нашли изоморфный подграф
            if not nodes_g1:
                return []

            result = []
            # Перебираем все узлы графа G1
            for n1 in nodes_g1:
                # Перебираем все узлы графа G2
                for n2 in nodes_g2:
                    # Если степени узлов совпадают, то продолжаем рекурсию
                    if g1[n1][0] == g2[n2][0]:
                        new_nodes_g1 = nodes_g1.copy()
                        new_nodes_g2 = nodes_g2.copy()
                        new_nodes_g1.remove(n1)
                        new_nodes_g2.remove(n2)
                        sub_results = _subgraph_isomorphism(g1, g2, new_nodes_g1, new_nodes_g2)
                        for sub_result in sub_results:
                            result.append([n1] + sub_result)
            return result

    # Получаем список узлов графа G1
    nodes_g1 = list(range(len(g1)))
    # Получаем список узлов графа G2
    nodes_g2 = list(range(len(g2)))
    # Запускаем рекурсивный поиск изоморфных подграфов
    return _subgraph_isomorphism(g1, g2, nodes_g1, nodes_g2)

# Определяем функцию для поиска максимального множества не пересекающихся изоморфных подграфов
def max_non_overlapping_subgraphs(g1, g2, subgraphs):
    # Внутренняя функция для рекурсивного поиска максимального множества не пересекающихся изоморфных подграфов
    def _max_non_overlapping_subgraphs(g1, g2, subgraphs, current_subgraphs):
        # Если subgraphs пуст, то мы нашли максимальное множество не пересекающихся изоморфных подграфов
        if not subgraphs:
            return current_subgraphs

        max_subgraphs = current_subgraphs.copy()
        max_size = len(current_subgraphs)

        # Перебираем все изоморфные подграфы
        for i in range(len(subgraphs)):
            subgraph = subgraphs[i]
            # Проверяем, не пересекается ли текущий подграф с уже найденными
            if not any(overlap_subgraph(g1, g2, subgraph, max_subgraph) for max_subgraph in max_subgraphs):
                new_subgraphs = subgraphs.copy()
                new_subgraphs.pop(i)
                max_subgraphs = _max_non_overlapping_subgraphs(g1, g2, new_subgraphs, current_subgraphs + [subgraph])
                if len(max_subgraphs) > max_size:
                    max_size = len(max_subgraphs)

        return max_subgraphs

    # Функция для проверки пересечения двух подграфов
    def overlap_subgraph(g1, g2, subgraph1, subgraph2):
        for n1 in subgraph1:
            for n2 in subgraph2:
                if g1[n1][0] == g2[n2][0] and n1 in subgraph2 and n2 in subgraph1:
                    return True
        return False

    # Получаем список изоморфных подграфов
    subgraphs = subgraph_isomorphism(g1, g2)
    # Запускаем рекурсивный поиск максимального множества не пересекающихся изоморфных подграфов
    return _max_non_overlapping_subgraphs(g1, g2, subgraphs, [])

# Пример использования
g1 = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
g2 = [(1, 2), (1, 3)]

max_subgraphs = max_non_overlapping_subgraphs(g1, g2, subgraph_isomorphism(g1, g2))
print(max_subgraphs)
