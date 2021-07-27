# Implementing Binary Tree.....

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def get_data(self):
        return self.data

    def get_right(self):
        return self.right

    def get_left(self):
        return self.left

    def set_data(self, data):
        self.data = data

    def set_right(self, right):
        self.right = right

    def set_left(self, left):
        self.left = left


class BinaryTree:

    def __init__(self, root=None):
        self.root = Node(root)

    def print_tree(self, data, level=0):
        if data != None:
            self.print_tree(data.get_left(), level + 1)
            print(' ' * 4 * level + '->', data.get_data())
            self.print_tree(data.get_right(), level + 1)

    def in_order(self, data):
        if data != None:
            self.in_order(data.get_left())
            print(data.get_data())
            self.in_order(data.get_right())

    def pre_order(self, data):
        if data != None:
            print(data.get_data())
            self.pre_order(data.get_left())
            self.pre_order(data.get_right())

    def post_order(self, data):
        if data != None:
            self.post_order(data.get_left())
            self.post_order(data.get_right())
            print(data.get_data())

    def get_root(self):
        return self.root

    def empty(self):
        if self.root is None:
            return True
        return False

    def get_node(self, data):
        current = None
        if not self.empty():
            current = self.get_root()
            while current is not None and current.get_data() is not data:
                if data < current.get_data():
                    current = current.get_left()
                else:
                    current = current.get_right()
        return current

    def get_min(self, root=None):
        if root is not None:
            curr_node = root
        else:
            curr_node = self.get_root()
        if not self.empty():
            curr_node = self.get_root()
            while curr_node.get_left() is not None:
                curr_node = curr_node.get_left()
        return curr_node

    def get_max(self, root=None):
        if root is not None:
            curr_node = root
        else:
            curr_node = self.get_root()
        if not self.empty():
            curr_node = self.get_root()
            while curr_node.get_right() is not None:
                curr_node = curr_node.get_right()
        return curr_node

    def insert(self, data):
        if self.root.get_data() is None:
            return self.root.set_data(data)
        new_node = Node(data)
        current = self.root
        while True:
            if data < current.get_data():
                if current.get_left() is None:
                    return current.set_left(new_node)
                current = current.get_left()
                continue
            elif data > current.get_data():
                if current.get_right() is None:
                    return current.set_right(new_node)
                current = current.get_right()
                continue
            return

    def delete(self, data):
        if not self.empty():
            node = self.get_node(data)
            if node is not None:
                if node.get_left() is None and node.get_right() is None:
                    node.set_data(0)

                elif node.get_left() is None and node.get_right() is not None:
                    root = node.get_right()
                    node.set_data(self.get_min(node.get_right()))
                    node.set_right(root)

                elif node.get_left() is not None and node.get_right() is None:
                    root = node.get_left().get_data()
                    self.delete(root)
                    node.set_data(root)

                else:
                    temp = self.get_max(node.get_left())
                    temporary = temp.get_data()
                    self.delete(temporary)
                    node.set_data(temporary)

    def search(self, data):
        node = self.root
        while node != None:
            if node.get_data() == data:
                return node.get_data()
            if node.get_data() > data:
                node = node.get_left()
            else:
                node = node.get_right()
        return False

    def predecessor(self, data):
        current = self.root
        prev = None
        if current.get_left() is not None:
            current = current.get_left()
            while current.get_right() is not None:
                current = current.get_left()
            prev = current
        elif current.get_right() is not None:
            current = current.get_right()
            while current.get_left() is not None:
                current = current.get_right()
            prev = current
        else:
            return None
        return prev.data

    def successor(self, data):
        current = self.root
        prev = None
        if current.get_right() is not None:
            current = current.get_right()
            while current.get_left() is not None:
                current = current.get_right()
            prev = current
        elif current.get_left() is not None:
            current = current.get_left()
            while current.get_right() is not None:
                current = current.get_left()
            prev = current
        else:
            return None
        return prev.data


b = BinaryTree()
b.insert(10)
b.insert(9)
b.insert(15)
b.insert(5)
b.insert(4)
b.insert(3)
b.insert(14)
b.insert(13)
b.insert(24)
b.print_tree(b.root)
print("InOrder...")
b.in_order(b.root)
print("PostOrder...")
b.post_order(b.root)
print("PreOrder...")
b.pre_order(b.root)
print("After Delete Node..")
b.delete(9)
b.print_tree(b.root)
print("Search Node : ", b.search(24))
print("Predecessor : ", b.predecessor(9))
print("Successor : ", b.successor(24))
