class SplayTree:
    def __init__(self):
        self.root = None

     def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y
 
    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
 
    def _splay(self, x):
        while x.parent is not None:
            p = x.parent
            g = p.parent
            if g is None:                          # zig
                if x == p.left:
                    self._right_rotate(p)
                else:
                    self._left_rotate(p)
            elif x == p.left and p == g.left:      # zig-zig
                self._right_rotate(g)
                self._right_rotate(p)
            elif x == p.right and p == g.right:    # zig-zig espejo
                self._left_rotate(g)
                self._left_rotate(p)
            elif x == p.right and p == g.left:     # zig-zag
                self._left_rotate(p)
                self._right_rotate(g)
            else:                                   # zig-zag espejo
                self._right_rotate(p)
                self._left_rotate(g)

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