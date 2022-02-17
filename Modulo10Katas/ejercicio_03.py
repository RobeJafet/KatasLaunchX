try:
    open("mars.jpg")
except FileNotFoundError as err:
    print("Tenemos un problema abriendo el archivo:", err)

    