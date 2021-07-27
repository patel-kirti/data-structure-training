# string = "ABCDEF"
#
#
# class Nodetree:
#     def __init__(self, left=None, right=None):
#         self.left = left
#         self.right = right
#
#     def child(self):
#         return self.left, self.right
#
#     def node(self):
#         return self.left, self.right
#
#     def __str__(self):
#         return "%s_%s" % self.left, self.right
#
#
# def huffman_code(node, left=True, bstring=' '):
#     if type(node) is str:
#         return {node: bstring}
#     (l, r) = node.child()
#     d = dict()
#     d.update(huffman_code(l, True, bstring + '0'))
#     d.update(huffman_code(r, False, bstring + '1'))
#     return d
#
#
# freq = {}
# for c in string:
#     if c in freq:
#         freq[c] += 1
#     else:
#         freq[c] = 1
# freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
# nodes = freq
# while len(nodes) > 1:
#     (key1, c1) = nodes[-1]
#     (key2, c2) = nodes[-2]
#     nodes = nodes[:-2]
#     node = Nodetree(key1, key2)
#     nodes.append((node, c1 + c2))
#     node = sorted(nodes, key=lambda x: x[1], reverse=True)
#
# h = huffman_code(nodes[0][0])
# print("Huffman Code...")
# for (char, frequency) in freq:
#     print(' %-4r |%12s' % (char, h[char]))


class node:
    def __init__(self, freq, symbol, right=None, left=None):
        self.freq = freq
        self.symbol = symbol
        self.right = right
        self.left = left
        self.huff = ''


def display(node, val=''):
    newval = val + str(node.huff)
    if node.left:
        display(node.left, newval)
    if node.right:
        display(node.right, newval)
    if not node.left and not node.right:
        print(f"{node.symbol}->{newval}")


char = ['a', 'b', 'c', 'd', 'e', 'f']
freq = [5, 9, 12, 13, 16, 45]
nodes = []
for x in range(len(char)):
    nodes.append(node(freq[x], char[x]))
while len(nodes) > 1:
    nodes = sorted(nodes, key=lambda x: x.freq)
    left = nodes[0]
    right = nodes[1]
    left.huff = 0
    right.huff = 1
    newnode = node(left.freq + right.freq, left.symbol + right.symbol, left, right)
    nodes.remove(left)
    nodes.remove(right)
    nodes.append(newnode)
display(nodes[0])
