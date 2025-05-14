def restar(*arg:int | float) -> int | float:
    resultado = arg[0]
    for i in arg[1:]:
        resultado -= i
    return resultado

if __name__ == "__main__":
    lista = [3, 5, 2, 5]
    resultado = restar(*lista)
    print(resultado)