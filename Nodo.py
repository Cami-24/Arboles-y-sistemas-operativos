class Nodo:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self.color = 1 # 1=Rojo, 0=Negro solo lo usa RedBlack


        