from typing import List


class Node:
    def __init__(self, key):
        self.key = key
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def __hash__(self):
        return self.key.__hash__()


class Tree:
    def __init__(self, key_pairs: List[tuple] = None):
        self.all_nodes = {}
        self.heads = set()
        for key_pair in key_pairs or []:
            self.add_node(key_pair[0], key_pair[1])

    def add_node(self, key, prev_key=None):
        if key in self.all_nodes:
            key_node = self.all_nodes[key]
        else:
            key_node = Node(key)
            self.heads.add(key_node)
            self.all_nodes[key] = key_node
        if prev_key:
            self.add_node(prev_key).add_child(key_node)
            if key_node in self.heads:
                self.heads.remove(key_node)
        return key_node

    @staticmethod
    def create_and_print_tree(key_pairs: List[tuple]):
        tree = Tree(key_pairs)
        tree.print_tree()
        return tree

    def print_tree(self):
        for head in self.heads:
            Tree._print_node_in_tree(head)
            print()

    @staticmethod
    def _print_node_in_tree(node, step=1):
        print("-" + str(node.key), end="")

        for num, child in enumerate(node.children):
            if num > 0:
                print("\n" + " " * step + "\\", end="")
            print("---", end="")
            Tree._print_node_in_tree(child, step + len(str(node.key)) + 4)


if __name__ == '__main__':
    Tree.create_and_print_tree(
        [("a", "b"), ("q", "b")]
    )
