def agua(agua_sobrante, astronautas, dias):
    for argument in [astronautas, agua_sobrante, dias]:
        try:
            argument / 10
        except TypeError:
            raise TypeError(f"Todos los argumentos necesitan ser de tipo entero, pero se recibio: '{argument}'")
    agua_diaria = astronautas * 11
    agua_total = agua_diaria * dias
    agua_total_sobrante = agua_sobrante - agua_total
    if agua_total_sobrante < 0:
        raise RuntimeError(f"No hay suficiente agua para {astronautas} astronautas despues {dias} dias")
    return f" El agua que durara despues de {dias} es : {agua_total_sobrante} litros"

agua("100", 5, "2")