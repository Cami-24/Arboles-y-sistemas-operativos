class SplayTree:
    def __init__(self):
        self.root = None

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