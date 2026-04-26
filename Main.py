def main():
    controller = Controller()
    controller.ejecutar()

    vista = Vista()
    vista.mostrar(controller.resultados)
    vista.graficar(controller.resultados)


if __name__ == "__main__":
    main()