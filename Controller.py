import random
import BST
import SplayTree
import RedBlakc
class Controller:
    def __init__(self):
        self.arboles = {
            "BST": BST(),
            "SplayTree": SplayTree(),
            "RedBlackTree": RedBlakc()
        }
        self.resultados = {}