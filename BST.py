class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        from Nodo import Nodo
        nuevo = Nodo(key)
        if self.root is None:
            self.root = nuevo
            return
        actual = self.root
        while True:
            if key < actual.data:
                if actual.left is None:
                    actual.left = nuevo
                    nuevo.parent = actual
                    return
                actual = actual.left
            else:
                if actual.right is None:
                    actual.right = nuevo
                    nuevo.parent = actual
                    return
                actual = actual.right

    def find(self, key):
        actual = self.root
        iteraciones = 0
        while actual is not None:
            iteraciones += 1
            if key == actual.data:
                return actual, iteraciones
            elif key < actual.data:
                actual = actual.left
            else:
                actual = actual.right
        return None, iteraciones