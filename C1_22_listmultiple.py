def list_multiple(a, b):
    if len(a) != len(b):
        raise(ZeroDivisionError)
        return None
    c = []
    for i in range(len(a)):
        c.append(a[i] * b[i])
    return c

a = [1, 2, 3]
b = [1, 2]
print(list_multiple(a, b))