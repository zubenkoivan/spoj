import math
import timeit


def odd_or_next(number, next_delta):
    return number if number & 1 == 1 else (number + next_delta)


def simple_sieve(limit):
    last_multiple = math.ceil(math.sqrt(limit))
    is_not_prime = [False for _ in range(limit)]
    primes = []

    for number in range(3, limit + 1, 2):
        if is_not_prime[number]:
            continue

        primes.append(number)

        if number > last_multiple:
            continue

        for not_prime in range(number * number, limit + 1, 2 * number):
            is_not_prime[not_prime] = True

    return primes


def print_interval_primes(start, end, primes, is_not_prime):
    if start == 2:
        print(2)

    start = odd_or_next(start, 1)
    end = odd_or_next(end, -1)
    size = end - start + 1

    for prime in primes:
        not_prime = prime * prime

        if not_prime > end:
            break
        elif not_prime < start:
            not_prime = ((start - 1) // prime + 1) * prime
            not_prime = odd_or_next(not_prime, prime)

        for number in range(not_prime - start, size, 2 * prime):
            is_not_prime[number] = True

    print('\n'.join(str(start + number)
                    for number in range(0, size, 2)
                    if not is_not_prime[number]))


def run():
    test_cases = int(input())
    intervals = [tuple(map(int, input().split())) for _ in range(test_cases)]
    primes = simple_sieve(int(math.sqrt(2147483647)))
    segment_size = int(math.ceil(math.sqrt(2147483647)))
    segment_buffer = [False for _ in range(segment_size)]

    for (start, end) in intervals:
        for segment_start in range(start, end, segment_size):
            for i in range(len(segment_buffer)):
                segment_buffer[i] = 0
            segment_end = min(segment_start + segment_size - 1, end)
            print_interval_primes(segment_start, segment_end, primes, segment_buffer)

run()
