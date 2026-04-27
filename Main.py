from BST import BST
from SplayTree import SplayTree
from RedBlakc import RedBlackTree
from Nodo import Nodo


def main():
    print("=== PRUEBA DE ÁRBOLES ===\n")

    # BST 
    print("BST:")
    bst = BST()

    # crear manual (porque no tienes insert aún)
    root = Nodo(10)
    root.left = Nodo(5)
    root.right = Nodo(15)

    bst.root = root

    nodo, pasos = bst.find(15)
    print("Resultado:", nodo.data if nodo else None)
    print("Pasos:", pasos)
    print()


    # SPLAY 
    print("Splay Tree:")
    splay = SplayTree()

    # igual que BST por ahora
    root = Nodo(10)
    root.left = Nodo(5)
    root.right = Nodo(15)

    splay.root = root

    nodo, pasos = splay.find(5)
    print("Resultado:", nodo.data if nodo else None)
    print("Pasos:", pasos)
    print()


    #RED BLACK
    print("Red-Black Tree:")
    rb = RedBlackTree()

    # aquí SÍ usar insert
    rb.insert(10)
    rb.insert(5)
    rb.insert(15)

    nodo, pasos = rb.find(10)
    print("Resultado:", nodo.data if nodo else None)
    print("Pasos:", pasos)
    print()


if __name__ == "__main__":
    main()