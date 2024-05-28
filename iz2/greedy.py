from itertools import combinations 

def subgraph_isomorphism_greedy(g1, g2):
    def isomorphic(sub_g1, sub_g2):
        if len(sub_g1) != len(sub_g2):
            return False
        vertex_mapping = {}
        for v1 in sub_g1:
            for v2 in sub_g2:
                if g1[v1][0] == g2[v2][0] and v2 not in vertex_mapping:
                    vertex_mapping[v2] = v1
                    break
            else:
              return False
        return all(g1[vertex_mapping[u]][1] == g2[v][1] for u, v in combinations(sub_g2, 2))

    def find_max_subgraph(g1, g2, sub_g1, sub_g2):
        max_sub_g1 = sub_g1.copy()
        max_sub_g2 = sub_g2.copy()
        for v1 in sub_g1:
            for v2 in sub_g2:
                if g1[v1][0] == g2[v2][0]:
                    new_sub_g1 = sub_g1.copy()
                    new_sub_g2 = sub_g2.copy()
                    new_sub_g1.remove(v1)
                    new_sub_g2.remove(v2)
                    if isomorphic(new_sub_g1, new_sub_g2):
                        sub_result = find_max_subgraph(g1, g2, new_sub_g1, new_sub_g2)
                        if len(sub_result[0]) > len(max_sub_g1):
                            max_sub_g1 = sub_result[0]
                            max_sub_g2 = sub_result[1]
        return max_sub_g1, max_sub_g2

    def find_all_subgraphs(g1, g2):
        subgraphs = []
        for i in range(len(g1)):
            for j in range(i + 1, len(g1)):
                sub_g1 = [i, j]
                sub_g2 = [0, 1]
                if isomorphic(sub_g1, sub_g2):
                    subgraphs.append((sub_g1, sub_g2))
        return subgraphs

    subgraphs = find_all_subgraphs(g1, g2)
    max_subgraphs = []
    while subgraphs:
        max_sub_g1, max_sub_g2 = find_max_subgraph(g1, g2, *subgraphs.pop())
        max_subgraphs.append(max_sub_g1)
    return max_subgraphs


g1 = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
g2 = [(1, 2), (1, 3)]

max_subgraphs = subgraph_isomorphism_greedy(g1, g2)
print(max_subgraphs)
