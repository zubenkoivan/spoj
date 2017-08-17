import sys


def create_sp2():
    result = [0, 2]
    is_prime = [True for _ in range(0, 4000)]
    for i in range(3, 7994, 2):
        if not is_prime[i // 2]:
            continue
        if (i & 3) == 1:
            result.append(i)
        for not_prime in range(i * i, 7994, i << 1):
            is_prime[not_prime // 2] = False
    return result


def create_p():
    result = [[0] * 7993 for _ in range(2)]
    for k in range(0, 2):
        result[k][0] = 1
        for i in range(1, 7993):
            result[k][i] += 2 if i <= k + 1 else 1
            max_part = min(k + 2, i)
            for part in range(2, max_part + 1):
                result[k][i] += result[part - 2][i - part]
    return result


def solve(n, k):
    if k == 1:
        return '1'
    return str(p[k - 2][sp2[n] - 1])


sp2 = create_sp2()
p = create_p()


def run():
    sys.stdin.readline()
    lines = filter(lambda x: not x.isspace(), sys.stdin.readlines())
    test_cases = map(lambda x: x.split(), lines)
    results = map(lambda x: solve(int(x[0]), int(x[1])), test_cases)
    sys.stdout.write('\n'.join(results))


run()