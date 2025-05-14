def suma(*arg:int | float) -> int | float:
    total = 0
    for i in arg:
        total += i
    return total

if __name__ == "__main__":
    numeros = [1,2,3,4,5]
    resultado = suma(*numeros)
    print(resultado)