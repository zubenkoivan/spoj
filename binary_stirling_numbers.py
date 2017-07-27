def run():
    test_cases = int(input())
    results = []

    for _ in range(test_cases):
        n, m = input().split()
        n, m = int(n), int(m)
        parity = int(((n - m) & ((m - 1) // 2)) == 0)
        results.append(str(parity))
    print('\n'.join(results))


run()