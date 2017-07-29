import math
import sys


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


def interval_primes(start, end, primes, is_prime):
    if start == 2:
        yield '2'

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
            is_prime[number // 2] = False
    for number in range(0, size, 2):
        if is_prime[number // 2]:
            yield str(start + number)
    yield ''


def run():
    sys.stdin.readline()
    lines = sys.stdin.readlines()
    intervals = map(lambda x: tuple(map(int, x.split())), lines)
    primes = simple_sieve(int(math.sqrt(2147483647)))
    segment_size = int(math.ceil(math.sqrt(2147483647)))
    segment_buffer_size = (segment_size - 1) // 2 + 1
    segment_buffer = [True for _ in range(segment_buffer_size)]

    for (start, end) in intervals:
        for segment_start in range(start, end, segment_size):
            for i in range(segment_buffer_size):
                segment_buffer[i] = True
            segment_end = min(segment_start + segment_size - 1, end)
            result = interval_primes(segment_start, segment_end, primes, segment_buffer)
            sys.stdout.write('\n'.join(result))

run()
