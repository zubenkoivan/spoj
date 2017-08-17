import sys
import math


def time(n, k, m):
    if m < n:
        return '0'
    result = math.log(m / n, k)
    return str(math.floor(result))


def run():
    sys.stdin.readline()
    test_cases = map(lambda x: x.split(), sys.stdin.readlines())
    test_cases = map(lambda x: (int(x[0]), int(x[1]), int(x[2])), test_cases)
    sys.stdout.write('\n'.join(map(lambda x: time(*x), test_cases)))


run()