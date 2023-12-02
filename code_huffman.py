import heapq
from collections import defaultdict
import matplotlib.pyplot as plt
import networkx as nx

class Node:
    def __init__(self, symbol=None, frequency=None, left=None, right=None):
        self.symbol = symbol
        self.frequency = frequency
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.frequency < other.frequency

def build_huffman_tree(data):
    frequency = defaultdict(int)
    for symbol in data:
        frequency[symbol] += 1

    heap = [Node(symbol, freq) for symbol, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(left.symbol + right.symbol, left.frequency + right.frequency, left, right)
        heapq.heappush(heap, merged)

    return heap[0]

def build_huffman_codes(node, current_code="", codes=None):
    if codes is None:
        codes = {}
    if node is not None:
        if node.symbol is not None:
            codes[node.symbol] = current_code
        build_huffman_codes(node.left, current_code + "0", codes)
        build_huffman_codes(node.right, current_code + "1", codes)
    return codes

def huffman_encode(data):
    root = build_huffman_tree(data)
    codes = build_huffman_codes(root)
    encoded_data = "".join(codes[symbol] for symbol in data)
    return encoded_data, root

def huffman_decode(encoded_data, root):
    decoded_data = ""
    current_node = root
    for bit in encoded_data:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.symbol is not None:
            decoded_data += current_node.symbol
            current_node = root

    return decoded_data

def plot_huffman_tree(node, pos=None, parent_node=None, graph=None, level=1, width=2., vert_gap = 0.2, xcenter = 0.5):
    if pos is None:
        pos = {node: (xcenter, 1 - level * vert_gap)}
    else:
        pos[node] = (xcenter, 1 - level * vert_gap)
    if graph is None:
        graph = nx.DiGraph()
    else:
        graph.add_edge(parent_node, node, length=width)
    neighbors = list(graph.neighbors(node))
    if len(neighbors) != 0:
        dx = width / 2 
        nextx = xcenter - width/2 - dx/2
        for neighbor in neighbors:
            nextx += dx
            pos = plot_huffman_tree(neighbor, pos=pos, parent_node=node,
                          graph=graph, level=level+1, width=dx, xcenter=nextx)
    return pos

# Example usage:
data = "abracadabra"
encoded_data, huffman_tree = huffman_encode(data)
decoded_data = huffman_decode(encoded_data, huffman_tree)

print("Original data:", data)
print("Encoded data:", encoded_data)
print("Decoded data:", decoded_data)

# Plotting the Huffman tree
graph = nx.DiGraph()
pos = plot_huffman_tree(huffman_tree, graph=graph)
nx.draw(graph, pos=pos, with_labels=True, arrows=False)
plt.show()
