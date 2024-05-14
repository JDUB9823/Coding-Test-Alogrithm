import sys
input = sys.stdin.readline

#root, left right
def preOrder(root):
    if root != ".":
        print(root, end = "")
        #left
        preOrder(tree[root][0])
        #right
        preOrder(tree[root][1])


#left, root, right
def inOrder(root):
    if root != ".":
        inOrder(tree[root][0])
        print(root, end = "")
        inOrder(tree[root][1])

#left, right, root
def postOrder(root):
    if root != ".":
        postOrder(tree[root][0])
        postOrder(tree[root][1])
        print(root, end = "")

N = int(input())
tree = {}

for _ in range(N):
    root, left, right = input().strip().split()
    tree[root] = [left, right]

preOrder("A")
print()
inOrder("A")
print()
postOrder("A")