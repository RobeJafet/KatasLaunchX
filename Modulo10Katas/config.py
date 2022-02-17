def main():
    try:
        configuration = open('config.txt')
    except Exception:
        print("No se pudo abrir config.txt ")
main()