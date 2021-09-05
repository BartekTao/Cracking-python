from typing import no_type_check
from binary_tree import BinaryTree
from binary_search_tree import BinarySearchTree



def is_binary_search_tree_v1(tree) -> bool:
    '''in-orderer取得node，並比較是否為小到大排序'''
    return _is_binary_search_tree_v1(tree.root)

def _is_binary_search_tree_v1(node, last_node = None) -> bool:
    if node is None:
        return True
    if not _is_binary_search_tree_v1(node.left, last_node):
        return False
    if last_node is not None and node.key <= last_node.key:
        return False
    last_node = node
    if not _is_binary_search_tree_v1(node.right, node):
        return False
    return True


def is_binary_search_tree_v2(tree) -> bool:
    #BST定義: root>leftAll，root<rightAll
    return _is_bst(tree.root, None, None)

def _is_bst(node, max, min) -> bool:
    if not node:
        return True
    if min and node.key < min:
        return False
    if max and node.key > max:
        return False

    #左邊 => 傳入最大值(head)，限制所有左邊的node都要小於最大值
    #右邊 => 傳入最小值(head)，限制所有右邊的node都要大於最小值
    return _is_bst(node.left, node.key, min) and _is_bst(node.right, max, node.key)



if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(20)
    bst.insert(9)
    bst.insert(25)
    bst.insert(5)
    bst.insert(12)
    bst.insert(11)
    bst.insert(14)

    t = BinaryTree()
    n1 = t.insert(5, None)
    n2 = t.insert(4, n1)
    n3 = t.insert(6, n1)
    n4 = t.insert(3, n2)
    t.insert(6, n2)
    t.insert(5, n3)
    t.insert(2, n4)

    print (is_binary_search_tree_v1(bst))
    print (is_binary_search_tree_v1(t))

    print (is_binary_search_tree_v2(bst))
    print (is_binary_search_tree_v2(t))
    
    