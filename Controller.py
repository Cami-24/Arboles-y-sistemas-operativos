import random
class Controller:
    def __init__(self):
        self.arboles = {
            "BST": BST(),
            "SplayTree": SplayTree(),
            "RedBlackTree": RedBlackTree()
        }
        self.resultados = {}