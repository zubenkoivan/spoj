import itertools as itr


def gcd(a, b):
    if a < b:
        (a, b) = (b, a)

    while True:
        mod = a % b

        if mod == 0:
            return b

        (a, b) = (b, mod)


def sum_proba(n, k):
    p = ((k - 1) // 2) * (k - 1 - (k - 1) // 2)
    q = n * (n - 1) // 2

    if p == 0:
        return "0"

    while True:
        divisor = gcd(p, q)

        if divisor == 1:
            return "{p}/{q}".format(p=p, q=q)

        p //= divisor
        q //= divisor


def run():
    input_stream = map(lambda x: tuple(map(int, input().split())), itr.count())
    input_stream = itr.takewhile(lambda x: x[0] != -1 or x[1] != -1, input_stream)

    for (n, k) in input_stream:
        print(sum_proba(n, k))


run()
