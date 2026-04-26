class NodoRB:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1 # 1=Rojo, 0=Negro
