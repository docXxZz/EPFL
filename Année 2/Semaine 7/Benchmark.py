#!/usr/bin/env python3
# Rappel : lancez avec `python3 -m pytest "Année 2/Semaine 7/Benchmark.py"`
# Si le plugin pytest-benchmark n'est pas installé, un fixture de secours est fourni ci-dessous.

# Fixture de secours pour `benchmark` si pytest-benchmark n'est pas présent
try:
    import pytest_benchmark  # type: ignore  # noqa: F401
except Exception:
    import pytest
    @pytest.fixture
    def benchmark():
        def _run(func):
            return func()
        return _run

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
    def append(self, value):
        if self.first is None:
            self.first = self.last = Node(value, None)
        else:
            self.last.next = Node(value, None)
            self.last = self.last.next
    def insert(self, index, value):
        previous = None
        current = self.first
        while index > 0 and current is not None:
            previous = current
            current = current.next
            index = index - 1
        if index > 0:
            raise IndexError('Index out of range')
        if previous is None:
            self.first = Node(value, current)
        else:
            previous.next = Node(value, current)
    def __getitem__(self, index): # quand on écrit `x[y]`, Python invoque `x.__getitem__(y)`
        current = self.first
        while index > 0 and current is not None:
            current = current.next
            index = index - 1
        if current is None:
            raise IndexError('Index out of range')
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
def ll_prepend():
    ll = LinkedList()
    # insérer au début équivaut à insert(0, n)
    for n in LIST:
        ll.insert(0, n)
    return ll

def ll_append():
    ll = LinkedList()
    for n in LIST:
        ll.append(n)
    return ll

# Les fonctions de benchmark doivent commencer par "test_" et prendre un paramètre "benchmark" qui est une fonction à appeler avec la fonction à benchmarker
def test_prepend(benchmark):
    benchmark(prepend)

def test_append(benchmark):
    benchmark(append)
def test_ll_prepend(benchmark):
    benchmark(ll_prepend)

def test_ll_append(benchmark):
    benchmark(ll_append)
