import sys


def get_numbers():
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67,
              71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139,
              149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223,
              227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293,
              307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383,
              389, 397, 401, 409, 419, 421, 431, 433, 439, 443]
    numbers = [0 for _ in range(2665)]
    for prime in primes:
        for number in range(prime, 2665, prime):
            numbers[number] += 1
    result = list(i for i in range(2665) if numbers[i] > 2)
    return result


def run():
    numbers = get_numbers()
    test_cases = int(sys.stdin.readline())
    results = map(lambda x: str(numbers[int(input()) - 1]), range(test_cases))
    sys.stdout.write('\n'.join(results))


run()
