def f(a, b):
    if a == b:
        return True
    if a > b:
        return False
    return f(a * 2, b) + f(a * 3, b)

print(f(8, 96) * f(96, 3456))