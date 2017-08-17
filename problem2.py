def white_balls_count(n, x, y):
    if n <= 1:
        return 'impossible'
    common = gcd(x, y)
    x = x // common
    y = y // common
    start = max([x, y]) + 1
    end = x + y - 1
    search_value = x**n + y**n
    while start <= end:
        mid = (start + end) // 2
        value = mid**n
        if value == search_value:
            return str(mid * common)
        if value < search_value:
            start = mid + 1
        else:
            end = mid - 1
    return 'impossible'


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def run():
    test_cases = int(input())
    test_cases = map(lambda _: input().split(), range(test_cases))
    counts = map(lambda x: white_balls_count(int(x[0]), int(x[1]), int(x[2])), test_cases)
    print('\n'.join(counts))


run()
