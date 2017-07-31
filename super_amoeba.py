import sys


def find_amoebas(test_cases):
    for test_case in test_cases:
        m, n = test_case
        c = 1000000007
        y = pow_mod(m, n, c)
        x = (((y - 1) % c) * (mod_inverse(m - 1, c) % c)) % c
        yield '%d %d' % (x, y)


def pow_mod(a, e, c):
    base = a % c
    result = 1
    while e > 0:
        if e & 1 == 1:
            result = (result * base) % c
        e = e >> 1
        base = (base * base) % c
    return result


def mod_inverse(a, c):
    r0, r1 = a, c
    s0, s1 = 1, 0
    while r1 > 0:
        q = r0 // r1
        r0, r1 = r1, r0 - q * r1
        s0, s1 = s1, s0 - q * s1
    return s0


def run():
    sys.stdin.readline()
    test_cases = map(lambda x: tuple(map(int, x.split())), sys.stdin.readlines())
    sys.stdout.write('\n'.join(find_amoebas(test_cases)))


run()
