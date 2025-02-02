class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Bst:
    def __init__(self):
        self.root = None

    def insert(self, value_to_insert):
        if self.root is None:
            self.root = Node(value_to_insert)
        else:
            #
            current_node = self.root
            while True:
                if value_to_insert < current_node.value:
                    if current_node.left is None:
                        current_node.left = Node(value_to_insert)
                        break

                    current_node = current_node.left
                else:
                    if current_node.right is None:
                        current_node.right = Node(value_to_insert)
                        break

                    current_node = current_node.right


def create_bst_from_array(A):
    binary_tree = Bst()

    for a in A:
        binary_tree.insert(a)

    return binary_tree

if __name__ == '__main__':
    A = [50, 30, 70, 20, 40, 60, 80]
    bst = create_bst_from_array(A)


