import sys
from enum import Enum, auto
from collections import namedtuple


Node = namedtuple('SetNode', ['value', 'color', 'parent', 'left', 'right'])

class Color(Enum):
    RED = auto()
    BLACK = auto()
    DOUBLE_BLACK = auto()


class Set(object):
    def __init__(self, *values):
        self._max = None
        self._root = None
        for value in values:
            self.insert(value)


    def insert(self, value):
        if value is None:
            return False
        if self._root is None:
            self._root = Node(value, Color.BLACK)
            self._max = value
            return True
        new_node = self._insert_leaf_node(value)
        if new_node is not None:
            self._balance(new_node)
            self._max = max(self._max, new_node.value)
            return True
        return False


    def _insert_leaf_node(self, value):
        curr = self._root
        parent = None
        is_left_child = None
        while curr is not None:
            if curr.value == value:
                return None
            parent = curr
            if value < curr.value:
                curr = curr.left
                is_left_child = True
            else:
                curr = curr.right
                is_left_child = False
        new_node = Node(value, color=Color.RED, parent=parent)
        if is_left_child:
            parent.left = new_node
        else:
            parent.right = new_node
        return new_node


    def _balance(self, node):
        while node.parent.color is Color.RED and node is not self._root:
            parent_sibling = Set._sibling(node.parent)
            if parent_sibling.color is Color.RED:
                node.parent.color = Color.BLACK
                parent_sibling.color = Color.BLACK
                node.parent.parent.color = Color.RED
                return
            if Set._is_left_child(node.parent):
                if Set._is_left_child(node):
                    node = Set._rotate_right(node.parent.parent)
                    node.left.color = Color.BLACK
                else:
                    node = Set._rotate_left(node.parent)
                    node = Set._rotate_right(node.parent)
                    node.left.color = Color.BLACK
            else:
                if Set._is_left_child(node):
                    node = Set._rotate_right(node.parent)
                    node = Set._rotate_left(node.parent)
                    node.right.color = Color.BLACK
                else:
                    node = Set._rotate_left(node.parent.parent)
                    node.right.color = Color.BLACK
        if node is self._root:
            self._root.color = Color.BLACK


    def remove(self, value):
        node = self._delete_node(value)
        if node is None:
            return
        while node.color is Color.DOUBLE_BLACK and node is not self._root:
            sibling = Set._sibling(node)
            if sibling.color is Color.BLACK:
                node.color = Color.BLACK
                if Set._any_red(sibling.left, sibling.right):
                    if Set._is_left_child(node):
                        if sibling.right is not None and sibling.right.color is Color.RED:
                            node = Set._rotate_left(node.parent)
                            node.right.color = Color.BLACK
                        else:
                            node = Set._rotate_right(sibling)
                            node = Set._rotate_left(node.parent)
                            node.color = Color.BLACK
                    else:
                        if sibling.left is not None and sibling.left.color is Color.RED:
                            node = Set._rotate_right(node.parent)
                            node.left.color = Color.BLACK
                        else:
                            node = Set._rotate_left(sibling)
                            node = Set._rotate_right(node.parent)
                            node.color = Color.BLACK
                    return
                else:
                    sibling.color = Color.RED
                    if node.parent.color is Color.RED:
                        node.parent.color = Color.BLACK
                        return
                    node = node.parent
                    node.color = Color.DOUBLE_BLACK
            else:
                sibling.color = Color.BLACK
                node.parent.color = Color.RED
                if Set._is_left_child(node):
                    Set._rotate_left(node.parent)
                else:
                    Set._rotate_right(node.parent)
        if node is self._root:
            self._root.color = Color.BLACK


    def _delete_node(self, value):
        node = self._find_node(value)
        if value is None:
            return None
        if node.left is not None and node.right is not None:
            min_node = Set._min_node(node.right)
            node.value = min_node.value
            node = min_node
        if node is self._root:
            self._root = node.left
            self._root.parent = None
            self._root.color = Color.BLACK
            return None
        parent = node.parent
        child = node.left or node.right
        if Set._is_left_child(node):
            parent.left = child
        else:
            parent.right = child
        if child is not None:
            child.parent = parent
            child.color = Color.BLACK
        if node.color is Color.BLACK and child is None:
            return Node(parent=parent, color=Color.DOUBLE_BLACK)
        return None


    def _find_node(self, value):
        node = self._root
        while node is not None:
            if node.value == value:
                return node
            node = node.left if value < node.value else node.right
        return None


    @staticmethod
    def _max_node(subtree_root):
        node = subtree_root
        while True:
            right = node.right
            if right is None:
                return node
            node = right


    @staticmethod
    def _min_node(subtree_root):
        node = subtree_root
        while True:
            left = node.left
            if left is None:
                return node
            node = left


    @staticmethod
    def _any_red(*nodes):
        for node in nodes:
            if node is not None and node.color is Color.RED:
                return True
        return False


    @staticmethod
    def _sibling(node):
        parent = node.parent
        return parent.right if Set._is_left_child(node) else parent.left


    @staticmethod
    def _is_left_child(node):
        if node.value is None:
            node = None
        return node is node.parent.left


    @staticmethod
    def _rotate_left(node):
        new_node_parent = node.parent
        new_left_right = node.right.left
        new_node = node.right
        new_left = node
        new_left.parent = new_node
        new_left.right = new_left_right
        if new_left.right is not None:
            new_left.right.parent = new_left
        new_node.left = new_left
        new_node.parent = new_node_parent
        return new_node


    @staticmethod
    def _rotate_right(node):
        new_node_parent = node.parent
        new_right_left = node.left.right
        new_node = node.left
        new_right = node
        new_right.parent = new_node
        new_right.left = new_right_left
        if new_right.left is not None:
            new_right.left.parent = new_right
        new_node.right = new_right
        new_node.parent = new_node_parent
        return new_node


    def lower_bound(self, value):
        node = self._root
        lower_bound = None
        while node is not None:
            if value == node.value:
                if node.left is not None:
                    lower_bound = Set._max_node(node.left)
                break
            if value < node.value:
                node = node.left
            else:
                lower_bound = node
                node = node.right
        return None if lower_bound is None else lower_bound.value


    def upper_bound(self, value):
        node = self._root
        upper_bound = None
        while node is not None:
            if value == node.value:
                if node.right is not None:
                    upper_bound = Set._min_node(node.right)
                break
            if value < node.value:
                upper_bound = node
                node = node.left
            else:
                node = node.right
        return None if upper_bound is None else upper_bound.value


    def max(self):
        return self._max


def solve(n, m, questions):
    x_coords = Set(0, n)
    y_coords = Set(0, m)
    x_intervals = Set(n)
    y_intervals = Set(m)
    for question in questions:
        line_type, line_coord = question
        if line_type == 0:
            max_x_interval = get_max_interval(line_coord, x_coords, x_intervals)
        else:
            max_y_interval = get_max_interval(line_coord, y_coords, y_intervals)
        yield get_area(max_x_interval, max_y_interval)


def get_max_interval(coord, coords, intervals):
    if not coords.insert(coord):
        return intervals.max()
    new_left = coord - coords.lower_bound(coord)
    new_right = coords.upper_bound(coord) - coord
    intervals.remove(new_left + new_right)
    intervals.insert(new_left)
    intervals.insert(new_right)
    return intervals.max()


def get_area(x_interval, y_interval):
    return (x_interval[1] - x_interval[0]) * (y_interval[1] - y_interval[0])


def get_questions(start, q, lines):
    for i in range(start, start + q):
        line = lines[i].split()
        yield (int(line[0]), int(line[1]))


def get_test_cases(lines):
    i = 0
    while i < len(lines):
        n, m, q = lines[i].split()
        n, m, q = int(n), int(m), int(q)
        i += 1
        yield (n, m, get_questions(i, q, lines))
        i += q


def run():
    sys.stdin.readline()
    results = map(lambda x: solve(*x), get_test_cases(sys.stdin.readlines()))
    sys.stdout.write('\n'.join(results))


run()