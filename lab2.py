
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
    

# min(n) = 3 + n*(1+2+2+2+1)
# max(n) = 3 + log2(n+1)*(1+log2(n+1)*(2+2+2)+1)           
def not_recursive(root):
    "Nodes counter"
    p = root  # 1
    v = [p]  # 1
    count = 0  # 1
    while v:  # log2(n+1)
        vn = []  # 1
        for x in v: 
            count += 1  # 2
            if x.left:
                vn.append(x.left)
            if x.right:
                vn.append(x.right)
            
        v = vn
    
    return count


# T(n) = 6*2^n-5
def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)



v = [10, 5, 7, 16, 13, 2, 20]

root = Node(v[0])

for x in v:
    push_tree(root, Node(x))


print(count_nodes(root))
print(not_recursive(root))