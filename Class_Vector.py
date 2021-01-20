u = (2, 3)
v = (7, 8)


def add(a, b):
    return (a[0]+b[0], a[1]+b[1])


def substract(a, b):
    return (a[0]-b[0], a[1]-b[1])


def dot(a, b):
    return (a[0]*b[0], a[1]*b[1])


def norm(a):
    return (a[0]*a[0] + a[1]*a[1]) ** 0.5


def isvertical(a):
    return a[0] == 0


print(norm(u))
print(add(u, v))
print(u + v)
print(isvertical(substract(v, u)))
