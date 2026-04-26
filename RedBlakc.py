class RedBlackTree:
    def __init__(self):
        self.NodoFantasma = Nodo(0)
        self.NodoFantasma.color = 0
        self.root = self.NodoFantasma

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NodoFantasma:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.NodoFantasma:
            x.right.parent = y
        x.parent = y.parent
        if y.parent == None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x
    
    def arreglar(self, k):
        while k.parent.color == 1: # Mientras mi padre sea Rojo
            if k.parent == k.parent.parent.left:
                u = k.parent.parent.right # Mi tío / tía
                if u.color == 1: # CASO 1: Mi Tío / Tía es Rojo
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent # Seguimos revisando al abuelo
                else:
                    if k == k.parent.right: # CASO 2: Triángulo
                        k = k.parent
                        self.left_rotate(k)
                    # CASO 3: Línea
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.right_rotate(k.parent.parent)
            else: # Simetría: el padre es hijo derecho
                u = k.parent.parent.left # Mi tío / tía
                if u.color == 1: # CASO 1: Mi Tío / Tía es Rojo
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.left: # CASO 2: Triángulo
                        k = k.parent
                        self.right_rotate(k)
                    # CASO 3: Línea
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.left_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 0 # Raíz siempre Negra

    def insert(self, key):
        # 1) Inserción normal BST
        nuevo_nodo = Nodo(key)
        nuevo_nodo.parent = None
        nuevo_nodo.left = self.NodoFantasma
        nuevo_nodo.right = self.NodoFantasma
        nuevo_nodo.color = 1

        padre = None
        actual = self.root

        while actual != self.NodoFantasma:
            padre = actual
            if nuevo_nodo.data < actual.data:
                actual = actual.left
            else:
                actual = actual.right

        nuevo_nodo.parent = padre
        if padre == None:
            self.root = nuevo_nodo
        elif nuevo_nodo.data < padre.data:
            padre.left = nuevo_nodo
        else:
            padre.right = nuevo_nodo

        # Si es la raíz, debe quedar negra
        if nuevo_nodo.parent == None:
            nuevo_nodo.color = 0
            return

        # Si no hay abuelo, no hay nada que arreglar.
        if nuevo_nodo.parent.parent == None:
            return

        # 2) Reparar propiedades rojo-negro
        self.arreglar(nuevo_nodo)

    def find(self, key):
        actual = self.root
        comparaciones = 0

        while actual != self.NodoFantasma:
            comparaciones += 1

            if key == actual.data:
                print(f"Nodo {key} encontrado despues de {comparaciones} comparaciones.")
                return actual, comparaciones

            if key < actual.data:
                actual = actual.left
            else:
                actual = actual.right

        print(f"Nodo {key} no encontrado despues de {comparaciones} comparaciones.")
        return None, comparaciones

    # def niveles(self):
    #     if self.root == self.NodoFantasma:
    #         return 0

    #     max_nivel = 0
    #     pila = [(self.root, 1)]

    #     while pila:
    #         nodo, nivel = pila.pop()
    #         if nivel > max_nivel:
    #             max_nivel = nivel

    #         if nodo.left != self.NodoFantasma:
    #             pila.append((nodo.left, nivel + 1))
    #         if nodo.right != self.NodoFantasma:
    #             pila.append((nodo.right, nivel + 1))

    #     return max_nivel

