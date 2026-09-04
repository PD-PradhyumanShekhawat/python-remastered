class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return

        self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:

            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)

        elif value > node.value:

            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None:
            return False

        if node.value == value:
            return True

        if value < node.value:
            return self._search_recursive(node.left, value)

        return self._search_recursive(node.right, value)

    def inorder(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node is None:
            return

        self._inorder_recursive(node.left, result)
        result.append(node.value)
        self._inorder_recursive(node.right, result)


if __name__ == "__main__":

    tree = BinarySearchTree()

    values = [50, 30, 70, 20, 40, 60, 80]

    for value in values:
        tree.insert(value)

    print("In-order traversal:")
    print(tree.inorder())

    print()

    search_values = [40, 65, 80]

    for value in search_values:
        print(
            f"Search {value}:",
            tree.search(value)
        )