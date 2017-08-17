import sys


def solve(n, i):
    return str(n**i - (n - 2)**i)

def run():
    sys.stdin.readline()
    test_cases = map(lambda x: x.split(), sys.stdin.readlines())
    results = map(lambda x: solve(int(x[0]), int(x[1])), test_cases)
    sys.stdout.write('\n'.join(results))


run()
