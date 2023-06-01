class TreeNode:
    def __init__(self, val, left=None, right=None):

        self.val = val
        self.leftchild = left
        self.rightchild = right


def build_tree():
    n = int(input())
    nodes = {}

    for _ in range(n):
        v, l, r = input().split()
        if v not in nodes:
            nodes[v] = TreeNode(v)
        if l != '.':
            if l not in nodes:
                nodes[l] = TreeNode(l)
                nodes[v].leftchild = nodes[l]
        if r != '.':
            if r not in nodes:
                nodes[r] = TreeNode(r)
                nodes[v].rightchild = nodes[r]

    return nodes['A']  # 루트 노드


def preorder(node):
    if node is None:
        return
    print(node.val, end="")
    preorder(node.leftchild)
    preorder(node.rightchild)


def inorder(node):
    if node is None:
        return
    inorder(node.leftchild)
    print(node.val, end="")
    inorder(node.rightchild)


def postorder(node):
    if node is None:
        return
    postorder(node.leftchild)
    postorder(node.rightchild)
    print(node.val, end="")


tree = build_tree()

preorder(tree)
print()
inorder(tree)
print()
postorder(tree)
