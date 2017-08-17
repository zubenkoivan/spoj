import sys


def factorial_mod(n, p):
    if n >= p:
        return '0'
    if n == p - 1:
        result = p - 1
    else:
        result = ((p - 1) * power_mod(product_mod(n + 1, p - 1, p), p - 2, p)) % p
    return str(result)


def power_mod(n, power, p):
    base = n
    result = 1
    while power > 0:
        if power & 1 == 1:
            result = (result * base) % p
        base = (base * base) % p
        power >>= 1
    return result


def product_mod(start, end, p):
    result = 1
    for n in range(start, end, 2):
        result = (result * (n * (n + 1)) % p) % p
    if (end - start) & 1 == 0:
        result = (result * end) % p
    return result

def run():
    sys.stdin.readline()
    test_cases = map(lambda x: x.split(), sys.stdin.readlines())
    results = map(lambda x: factorial_mod(int(x[0]), int(x[1])), test_cases)
    sys.stdout.write('\n'.join(results))


run()