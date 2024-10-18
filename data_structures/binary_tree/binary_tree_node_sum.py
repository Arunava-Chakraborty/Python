from __future__ import annotations
from collections.abc import Iterator


class Node:
    """
    A Node has a value variable and pointers to Nodes to its left and right.
    """

    def __init__(self, value: int) -> None:
        self.value: int = value
        self.left: Node | None = None
        self.right: Node | None = None


class BinaryTreeNodeSum:
    """
    A class to calculate the sum of all nodes in a binary tree.
    """

    def __init__(self, tree: Node) -> None:
        self.tree = tree

    @staticmethod
    def depth_first_search(node: Node | None) -> int:
        """Recursively calculates the sum of the tree nodes."""
        if node is None:
            return 0
        # Sum the current node's value and the values from left and right subtrees
        return node.value + BinaryTreeNodeSum.depth_first_search(node.left) + BinaryTreeNodeSum.depth_first_search(node.right)

    def total_sum(self) -> int:
        """Returns the total sum of the binary tree nodes."""
        return self.depth_first_search(self.tree)

    def __iter__(self) -> Iterator[int]:
        yield self.total_sum()


if __name__ == "__main__":
    import doctest

    doctest.testmod()
