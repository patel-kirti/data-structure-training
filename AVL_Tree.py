class Node:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data
        self.height = 0


class Avl:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if 0 < data and data < 100:
            self.root = self.insert_node(data, self.root)
        else:
            print("Out of range")

    def insert_node(self, data, node):
        if not node:
            return Node(data)
        if data < node.data:
            node.left = self.insert_node(data, node.left)
        else:
            node.right = self.insert_node(data, node.right)
        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
        return self.settlevolation(data, node)

    def settlevolation(self, data, node):
        balance = self.get_balance(node)
        if balance > 1 and data < node.left.data:
            return self.right_roted(node)
        if balance < -1 and data > node.right.data:
            return self.left_roted(node)
        if balance > 1 and data > node.left.data:
            node.left = self.left_roted(node.left)
            return self.right_roted(node)
        if balance < -1 and data < node.right.data:
            node.right = self.right_roted(node.right)
            return self.left_roted(node)
        return node

    def remove(self, data):
        if self.root:
            self.root = self.remove_node(data, self.root)

    def remove_node(self, data, node):
        if not node:
            return node
        if data < node.data:
            node.left = self.remove_node(data, node.left)
        if data > node.data:
            node.right = self.remove_node(data, node.right)
        else:
            if not node.left and not node.right:
                del node
                return None
            if not node.left:
                temp = node.right
                del node
                return temp
            if not node.right:
                temp = node.left
                del node
                return temp
            temp = self.getpredecessor(node.left)
            node.data = temp.data
            node.left = self.remove_node(temp.data, node.left)
        if not node:
            return node
        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
        balance = self.get_balance(node)

        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.right_roted(node)

        if balance < -1 and self.get_balance(node.right) <= 0:
            return self.left_roted(node)

        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.left_roted(node.left)
            return self.right_roted(node)

        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.right_roted(node.right)
            return self.left_roted(node)
        return node

    def get_height(self, node):
        if not node:
            return -1

        return node.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def right_roted(self, node):
        templ = node.left
        t = templ.right
        templ.right = node
        node.left = t
        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
        templ.height = max(self.get_height(templ.left), self.get_height(templ.right)) + 1
        return templ

    def left_roted(self, node):
        tempr = node.right
        t = tempr.left
        tempr.left = node
        node.right = t
        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
        tempr.height = max(self.get_height(tempr.left), self.get_height(tempr.right)) + 1
        return tempr

    def getpredecessor(self, node):
        if node.right:
            return self.getpredecessor(node.right)
        return node

    def traverse(self):
        if self.root:
            print("InOrder...")
            self.inorder(self.root)
            print("PreOrder...")
            self.preorder(self.root)
            print("PostOrder...")
            self.postorder(self.root)

    def inorder(self, node, level=0):
        if node.left:
            self.inorder(node.left, level + 1)
        print(' ' * 5 * level + '~', node.data)
        if node.right:
            self.inorder(node.right, level + 1)

    def preorder(self, node):
        print(node.data)
        if node.left:
            self.preorder(node.left)
        if node.right:
            self.preorder(node.right)

    def postorder(self, node):
        if node.left:
            self.postorder(node.left)
        if node.right:
            self.postorder(node.right)
        print(node.data)


n = Avl()
n.insert(99)
n.insert(54)
n.insert(45)
n.insert(60)
n.insert(7)
n.insert(10)
n.insert(22)
n.insert(39)
n.insert(11)
n.insert(3)
n.insert(64)
n.insert(69)
n.insert(82)
n.insert(91)
n.insert(95)
n.insert(75)
n.traverse()
print("Remove Node...")
n.remove(82)
n.traverse()
