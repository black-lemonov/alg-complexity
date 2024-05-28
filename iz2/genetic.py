import random
import itertools
from igraph import Graph

g1 = Graph()
g1.add_vertices(5)
g1.add_edges([(0, 1), (1, 2), (2, 3), (3, 0), (3, 4)])

g2 = Graph()
g2.add_vertices(4)
g2.add_edges([(0, 1), (1, 2), (2, 3)])

def isomorphic(sub_g1, sub_g2):
    """
    Checks if two subgraphs are isomorphic.
    """
    if len(sub_g1) != len(sub_g2):
        return False
    vertex_mapping = {}
    for v1 in sub_g1:
        for v2 in sub_g2:
            if sub_g1.degree(v1) == sub_g2.degree(v2) and v2 not in vertex_mapping:
                vertex_mapping[v2] = v1
                break
        else:
            return False
    return all(sub_g1.degree(vertex_mapping[u]) == sub_g2.degree(v) for u, v in itertools.combinations(sub_g2, 2))

def fitness(chromosome):
    """
    Calculates the fitness of a chromosome.
    """
    subgraphs = [g1.subgraph(c) for c in chromosome]
    count = 0
    for i in range(len(chromosome)):
        for j in range(i + 1, len(chromosome)):
            if isomorphic(subgraphs[i].es, subgraphs[j].es):
                count += 1
    return count

def mutate(chromosome):
    """
    Mutates a chromosome by swapping two random genes.
    """
    i, j = random.sample(range(len(chromosome)), 2)
    chromosome[i], chromosome[j] = chromosome[j], chromosome[i]

def crossover(parent1, parent2):
    """
    Performs crossover on two parents to produce a child.
    """
    crossover_point = random.randint(1, len(parent1) - 1)
    child = parent1[:crossover_point] + [node for node in parent2 if node not in parent1[:crossover_point]]
    return child

def select_parent(population):
    """
    Selects a parent based on fitness.
    """
    return max(population, key=fitness)

def generate_initial_population(population_size, graph_size):
    """
    Generates an initial population of random chromosomes.
    """
    return [random.sample(range(graph_size), k=2) for _ in range(population_size)]

def genetic_algorithm(graph_size, population_size, mutation_rate, generations):
    """
    Runs the genetic algorithm to find the maximum subset of isomorphic subgraphs.
    """
    population = generate_initial_population(population_size, graph_size)

    for _ in range(generations):
        population = sorted(population, key=fitness, reverse=True)
        new_population = []

        for _ in range(population_size // 2):
            parent1 = select_parent(population)
            parent2 = select_parent(population)

            if random.random() < mutation_rate:
                child = crossover(parent1, parent2)
                mutate(child)
            else:
                child = crossover(parent1, parent2)

            new_population.append(child)

        population = new_population

    return population


g1 = Graph([(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)])
g2 = Graph([(1, 2), (1, 3)])

max_subgraphs = genetic_algorithm(g1.vcount(), 100, 0.1, 100)
print(set(max_subgraphs))
