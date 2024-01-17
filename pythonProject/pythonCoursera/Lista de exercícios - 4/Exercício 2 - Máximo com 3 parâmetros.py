def maximo(x, y, z):
    if x > y and x > z:
        m = x
    elif y > x and y > z:
        m = y
    elif z > x and z > y:
        m = z
    elif x == y and x == z:
        m = z

    return m


print(maximo(7, 7, 7))