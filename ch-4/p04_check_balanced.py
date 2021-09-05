#檢查二元樹是否平衡

class BinaryNode:
    def __init__(self, name) -> None:
        self.name = name
        self.left = None
        self.right = None

def is_balanced(node) -> bool:
    return checkHeight(node) != -(10 ** 100)

def checkHeight(node) -> int:
    min = -(10 ** 100)
    if node is None:
        return -1
    leftHeight = checkHeight(node.left)
    if leftHeight == min:
        return min
    rightHeight = checkHeight(node.right)
    if rightHeight == min:
        return min
    
    heightDiff = abs(leftHeight - rightHeight)
    if heightDiff > 1:
        return min
    else:
        return max(leftHeight, rightHeight)+1

def _gen_unbalanced_1():
    root = BinaryNode(1)
    root.left = BinaryNode(2)
    root.left.left = BinaryNode(4)
    root.left.right = BinaryNode(5)
    root.left.right.right = BinaryNode(6)
    root.left.right.right.right = BinaryNode(7)
    root.right = BinaryNode(3)
    root.right.left = BinaryNode(8)
    root.right.right = BinaryNode(9)
    root.right.right.right = BinaryNode(10)
    root.right.right.right.right = BinaryNode(11)
    return root

def _gen_balanced_1():
    root = BinaryNode(1)
    root.left = BinaryNode(2)
    return root


def _gen_balanced_2():
    root = BinaryNode(7)
    root.left = BinaryNode(2)
    root.left.left = BinaryNode(4)
    root.right = BinaryNode(3)
    root.right.left = BinaryNode(8)
    root.right.right = BinaryNode(9)
    root.right.right.right = BinaryNode(10)
    return root

if __name__ == "__main__":
    test = _gen_balanced_2()
    is_balanced(test)
    print(is_balanced(test))

    