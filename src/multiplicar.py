def multiplicar(*arg: int | float) -> int | float:
    total = arg[0]
    for i in arg[1:]:
        total *= i
    return total

if __name__ == "__main__":
    arg = [4, 2, 6]
    resultado = multiplicar(*arg)
    print(resultado)