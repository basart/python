def h(x, y, *args, **kwargs):
    print('x={}, y={}, args={}, kwargs={}'.format(x, y, args, kwargs))

h(1, 2)

h(1, 2, 3)
h(1, 2, z=3)
h(1, 2, 3, z=4)

def sum(*args):
    s = 0
    for item in args:
        s += item
    return s
print sum(1, 2, 4)