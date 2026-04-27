class SplayTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        from Nodo import Nodo
        nuevo = Nodo(key)
        if self.root is None:
            self.root = nuevo
            return
        actual = self.root
        padre = None
        while actual is not None:
            padre = actual
            if key < actual.data:
                actual = actual.left
            else:
                actual = actual.right
        nuevo.parent = padre
        if key < padre.data:
            padre.left = nuevo
        else:
            padre.right = nuevo
        self._splay(nuevo)

    def find(self, key):
        actual = self.root
        iteraciones = 0

        while actual is not None:
            iteraciones += 1

            if key == actual.data:
                # splay vacío por ahora
                return actual, iteraciones

            elif key < actual.data:
                actual = actual.left
            else:
                actual = actual.right

        return None, iteraciones