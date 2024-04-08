import time

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = self.right = None


def push_tree(root, obj):
    if root is None: return

    if obj.data == root.data: return 

    if obj.data > root.data:
        if root.right:
            push_tree(root.right, obj)
        else:
            root.right = obj
            return
    if obj.data < root.data:
        if root.left:
            push_tree(root.left, obj)
        else:
            root.left = obj
            return
        
def make_tree(v):
    root = Node(v[0])
    for x in v:
        push_tree(root, Node(x))
    
    return root

# измерение времени работы
def get_time(f, *args):
    repeat = 10000000
    total = []
    for _ in range(repeat):
        start_time = time.time()
        f(args[0])  
        end_time = time.time()
        execution_time = end_time - start_time
        total.append(execution_time)
    
    average_time = sum(total)/repeat
    return average_time
    

# рекурсивный алгоритм
def find_diff(node): 
    if node.left and node.right:
        return find_diff(node.left) + find_diff(node.right)
    if node.left and node.right is None:
        return 1 + find_diff(node.left)
    if node.left is None and node.right:
        return find_diff(node.right) - 1
    if node.left is None and node.right is None:
        return 0


# деревья для экспериментальных расчетов
# полные деревья
full_trees = [
    [1],
    [2, 1, 3],
    [4, 2, 1, 3, 6, 5, 7],
    [8, 4, 2, 1, 3, 6, 5, 7, 12, 10, 9, 11, 14, 13, 15]
]

# вырожденные деревья 
degen_trees = [
    [1],
    [1, 2],
    [1, 2, 3],
    [1, 2, 3, 4]
]

print("Полные деревья:")
for v in full_trees:
    t = make_tree(v)
    print(f'n = {len(v):2}  T = {get_time(find_diff, t)}')

print("Вырожденные деревья:")
for v in degen_trees:
    t = make_tree(v)
    print(f'n = {len(v)}  T = {get_time(find_diff, t)}')

