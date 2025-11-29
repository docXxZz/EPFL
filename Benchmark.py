#!/usr/bin/env python3
# Rappel : lancez avec `python3 -m pytest benchmark.py`

LIST = list(range(0, 10000))

# Implémentation basique d'une liste chaînée (pas encore utilisée dans les benchmarks ci dessous)
# Créer avec p.ex. `result = LinkedList()`,
# puis utilisez p.ex. `result[1]`, `result.append(42)` et `result.insert(0, 123)`, comme une `list` intégrée à Python.
# (Il manque beaucoup de méthodes que les listes Python ont, cette classe n'existe que pour cet exercice)
class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next
class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0

    def __len__(self):
        return self._size

    def __iter__(self):
        current = self.first
        while current is not None:
            yield current.value
            current = current.next

    def append(self, value):
        node = Node(value, None)
        if self.first is None:
            self.first = self.last = node
        else:
            self.last.next = node
            self.last = node
        self._size += 1

    def prepend(self, value):
        node = Node(value, self.first)
        self.first = node
        if self.last is None:
            self.last = node
        self._size += 1

    def insert(self, index, value):
        # Semantics similar to Python list: index <= 0 inserts at head,
        # index >= len inserts at tail, otherwise in the middle.
        if self.first is None or index <= 0:
            # insert at head
            node = Node(value, self.first)
            self.first = node
            if self.last is None:
                self.last = node
            self._size += 1
            return

        # Walk to the node just before the desired index, or to the tail
        prev = self.first
        i = 1
        while i < index and prev.next is not None:
            prev = prev.next
            i += 1
        # Insert after prev
        node = Node(value, prev.next)
        prev.next = node
        if node.next is None:
            # inserted at tail
            self.last = node
        self._size += 1

    def __getitem__(self, index):  # quand on écrit `x[y]`, Python invoque `x.__getitem__(y)`
        # Support negative indices
        if self._size == 0:
            raise IndexError('Index out of range')
        if index < 0:
            index += self._size
        if index < 0 or index >= self._size:
            raise IndexError('Index out of range')
        current = self.first
        for _ in range(index):
            current = current.next
        return current.value

def prepend():
    result = []
    for n in LIST:
        result.insert(0, n) # ajoute `n` au début de la liste
    return result

def append():
    result = []
    for n in LIST:
        result.append(n)
    return result


# Les fonctions de benchmark doivent commencer par "test_" et prendre un paramètre "benchmark" qui est une fonction à appeler avec la fonction à benchmarker
def test_prepend(benchmark):
    benchmark(prepend)

def test_append(benchmark):
    benchmark(append)

# Variantes utilisant la LinkedList ci-dessus

def llist_prepend():
    result = LinkedList()
    for n in LIST:
        result.prepend(n)
    return result


def llist_append():
    result = LinkedList()
    for n in LIST:
        result.append(n)
    return result


def test_llist_prepend(benchmark):
    benchmark(llist_prepend)


def test_llist_append(benchmark):
    benchmark(llist_append)


def test_linkedlist_sanity():
    # petit test de cohérence pour LinkedList
    ll = LinkedList()
    ll.append(1)
    ll.insert(0, 0)
    ll.insert(999, 2)
    assert list(ll) == [0, 1, 2]
    assert ll[-1] == 2
    import pytest
    with pytest.raises(IndexError):
        _ = ll[3]
