def main():
    try:
        texto = open('texto.txt')
    except FileNotFoundError:
        print("No se encontro el archivo .txt")

main()