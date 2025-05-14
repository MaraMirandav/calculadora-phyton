def suma(*arg:int | float) -> int | float:
    total = 0
    for i in arg:
        total += i
    return total