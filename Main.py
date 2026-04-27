import random
import math
import matplotlib.pyplot as plt
from graphviz import Digraph
import os
 
from BST import BST
from SplayTree import SplayTree
from RedBlakc import RedBlackTree
from Nodo import Nodo
 
 
# ─────────────────────────────────────────────────────────────
# VISUALIZACIÓN
# ─────────────────────────────────────────────────────────────
def visualizar_bst(arbol, titulo, nombre_archivo, max_nodos=60):
    dot = Digraph(comment=titulo)
    dot.attr(rankdir='TB', size='14,10')
    dot.attr('node', shape='circle', style='filled', fillcolor='#4A90D9',
             fontcolor='white', fontsize='10', width='0.4', height='0.4')
    dot.attr('edge', color='#555555', arrowsize='0.6')
 
    if arbol.root is None:
        return
 
    cola = [arbol.root]
    visitados = 0
    while cola and visitados < max_nodos:
        nodo = cola.pop(0)
        visitados += 1
        dot.node(str(id(nodo)), str(nodo.data))
        if nodo.left:
            dot.edge(str(id(nodo)), str(id(nodo.left)))
            cola.append(nodo.left)
        if nodo.right:
            dot.edge(str(id(nodo)), str(id(nodo.right)))
            cola.append(nodo.right)
 
    dot.attr(label=f'{titulo}\n(mostrando {min(visitados, max_nodos)} de 1000 nodos)',
             labelloc='t', fontsize='14')
    dot.render(nombre_archivo, format='png', cleanup=True)
    print(f"    -> {nombre_archivo}.png")
    os.startfile(f"{nombre_archivo}.png")  # Open the PNG file
 
 
def visualizar_rb(arbol, titulo, nombre_archivo, max_nodos=60):
    dot = Digraph(comment=titulo)
    dot.attr(rankdir='TB', size='14,10')
    dot.attr('edge', color='#555555', arrowsize='0.6')
 
    fantasma = arbol.NodoFantasma
    cola = [arbol.root]
    visitados = 0
    while cola and visitados < max_nodos:
        nodo = cola.pop(0)
        if nodo == fantasma:
            continue
        visitados += 1
        color_fill = '#C0392B' if nodo.color == 1 else '#2C3E50'
        dot.node(str(id(nodo)), str(nodo.data),
                 style='filled', fillcolor=color_fill,
                 fontcolor='white', shape='circle',
                 fontsize='10', width='0.4', height='0.4')
        if nodo.left and nodo.left != fantasma:
            dot.edge(str(id(nodo)), str(id(nodo.left)))
            cola.append(nodo.left)
        if nodo.right and nodo.right != fantasma:
            dot.edge(str(id(nodo)), str(id(nodo.right)))
            cola.append(nodo.right)
 
    dot.attr(label=f'{titulo}\n(mostrando {min(visitados, max_nodos)} de 1000 nodos)',
             labelloc='t', fontsize='14')
    dot.render(nombre_archivo, format='png', cleanup=True)
    print(f"    -> {nombre_archivo}.png")
    os.startfile(f"{nombre_archivo}.png")  # Open the PNG file
 
 
# ─────────────────────────────────────────────────────────────
# ESCENARIO A – Llegada aleatoria
# ─────────────────────────────────────────────────────────────
def escenarioA():
    print("=" * 55)
    print("  ESCENARIO A - Llegada Aleatoria (1 000 procesos)")
    print("=" * 55)
 
    N      = 1000
    SEED   = 42
    BUSCAR = 100
 
    random.seed(SEED)
    vruntimes = random.sample(range(1, 10_001), N)
 
    # Insercion
    print("\n[1] Insertando procesos...")
    bst   = BST()
    splay = SplayTree()
    rb    = RedBlackTree()
 
    for v in vruntimes:
        bst.insert(v)
        splay.insert(v)
        rb.insert(v)
 
    # Visualizacion
    print("\n[2] Visualizando estructura (60 nodos superficiales)...")
    visualizar_bst(bst,   "BST - Escenario A",            "arbol_BST_A")
    visualizar_bst(splay, "Splay Tree - Escenario A",     "arbol_Splay_A")
    visualizar_rb(rb,     "Red-Black Tree - Escenario A", "arbol_RB_A")
 
    # Busquedas
    print("\n[3] Buscando 100 procesos aleatorios...")
    random.seed(SEED + 1)
    muestra = random.sample(vruntimes, BUSCAR)
 
    resultados = {"BST": [], "Splay Tree": [], "Red-Black Tree": []}
    for key in muestra:
        _, it = bst.find(key)
        resultados["BST"].append(it)
        _, it = splay.find(key)
        resultados["Splay Tree"].append(it)
        _, it = rb.find(key)
        resultados["Red-Black Tree"].append(it)
 
    # Estadisticas
    print("\n[4] Resultados:")
    print(f"  {'Arbol':<18} {'Prom':>8} {'Min':>6} {'Max':>6}  log2(1000)~10.0")
    print("  " + "-" * 46)
    for nombre, iters in resultados.items():
        prom = sum(iters) / len(iters)
        print(f"  {nombre:<18} {prom:>8.2f} {min(iters):>6} {max(iters):>6}")
 
    # Grafica
    print("\n[5] Generando grafica...")
    nombres   = list(resultados.keys())
    promedios = [sum(v) / len(v) for v in resultados.values()]
    colores   = ["#4A90D9", "#27AE60", "#8E44AD"]
    log_n     = math.log2(N)
 
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    fig.suptitle("Escenario A - Llegada Aleatoria (1 000 procesos, 100 busquedas)",
                 fontsize=13, fontweight='bold', y=1.02)
 
    ax1 = axes[0]
    bars = ax1.bar(nombres, promedios, color=colores, width=0.5,
                   edgecolor='black', linewidth=0.7)
    ax1.axhline(log_n, color='red', linestyle='--', linewidth=1.5,
                label=f'O(log2 n) ~ {log_n:.1f}')
    for bar, val in zip(bars, promedios):
        ax1.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.1,
                 f'{val:.2f}', ha='center', va='bottom', fontsize=11, fontweight='bold')
    ax1.set_ylabel("Iteraciones promedio", fontsize=11)
    ax1.set_title("Promedio de iteraciones por busqueda", fontsize=11)
    ax1.legend(fontsize=10)
    ax1.set_ylim(0, max(promedios) * 1.35)
    ax1.grid(axis='y', linestyle='--', alpha=0.4)
 
    ax2 = axes[1]
    bp = ax2.boxplot(list(resultados.values()), tick_labels=nombres,
                     patch_artist=True,
                     medianprops=dict(color='black', linewidth=2))
    for patch, color in zip(bp['boxes'], colores):
        patch.set_facecolor(color)
        patch.set_alpha(0.75)
    ax2.axhline(log_n, color='red', linestyle='--', linewidth=1.5,
                label=f'O(log2 n) ~ {log_n:.1f}')
    ax2.set_ylabel("Iteraciones", fontsize=11)
    ax2.set_title("Distribucion de iteraciones", fontsize=11)
    ax2.legend(fontsize=10)
    ax2.grid(axis='y', linestyle='--', alpha=0.4)
 
    plt.tight_layout()
    plt.savefig("escenario_A_comparacion.png", dpi=150, bbox_inches='tight')
    plt.show()  # Add this to display the plot
    plt.close()
    print("    -> escenario_A_comparacion.png")
    print("\n Escenario A completado.\n")



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


    #Escenarios
    escenarioA()


if __name__ == "__main__":
    main()