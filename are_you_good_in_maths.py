import math


def find_triangle(h, a):
    step1 = h**4 / 4 - 4 * a**2
    if step1 < 0:
        return '-1'
    leg1 = math.sqrt(math.sqrt(step1) + h**2 / 2)
    leg2 = 2 * a / leg1
    if leg2 < leg1:
        leg1, leg2 = leg2, leg1
    return '%.6f %.6f %d' % (leg1, leg2, h)


def read_test_cases():
    test_cases = int(input())
    for _ in range(test_cases):
        h, a = input().split()
        h, a = int(h), int(a)
        yield (h, a)


def run():
    triangles = map(lambda x: find_triangle(*x), read_test_cases())
    print('\n'.join(triangles))


run()