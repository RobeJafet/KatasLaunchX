def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("No se encontro el archivo config.txt")
    except PermissionError:
        print("Se encontro config.txt, pero no se puede leer")

main()