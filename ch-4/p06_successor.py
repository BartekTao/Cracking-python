from binary_search_tree import BinarySearchTree

def successor(treeNode):
    if not treeNode:
        return None
    if treeNode.right:
        return mostLeftNode(treeNode.right)
    else:
        #向上直到位在left subtree為止
        temp = treeNode
        parent = temp.parent
        while parent and parent.right == temp:
            tempt = parent
            parent = parent.parent
        return parent

def mostLeftNode(node):
    if not node:
        return None
    while node.left:
        node = node.left
    return node

if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(20)
    bst.insert(9)
    bst.insert(25)
    bst.insert(5)
    bst.insert(12)
    bst.insert(11)
    bst.insert(14)
    print(successor(bst.root.left).key)

