import matplotlib.pyplot as plt

class Vista:
    def mostrar(self, resultados):
        for arbol, datos in resultados.items():
            print(arbol, datos)