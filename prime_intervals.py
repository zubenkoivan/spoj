import math


def simple_sieve(n):

    last_multiple = math.ceil(math.sqrt(n))

    is_prime = [True for _ in range(2, n + 1)]
    prime_numbers = []

    for number in range(2, n + 1):

        if not is_prime[number - 2]:
            continue

        prime_numbers.append(number)

        if number > last_multiple:
            continue

        for multiple in range(number, n + 1, number):
            is_prime[multiple - 2] = False

    return prime_numbers


def segmented_sieve(base_primes, start, end):

    interval_size = math.ceil(math.sqrt(end))
    is_prime = [True for _ in range(interval_size)]
    prime_numbers = []

    for interval_start in range(start, end + 1, interval_size):
        for i in range(len(is_prime)):
            is_prime[i] = True

        interval_end = min(end, interval_start + interval_size - 1)

        for base_prime in base_primes:
            first_multiple = math.ceil(interval_start / base_prime) * base_prime

            if first_multiple == base_prime:
                first_multiple += base_prime

            for number in range(first_multiple, interval_end + 1, base_prime):
                is_prime[number - interval_start] = False

        for number in range(interval_start, interval_end + 1):
            if is_prime[number - interval_start]:
                prime_numbers.append(number)

    return prime_numbers


def run():
    test_cases = int(input())
    intervals = [tuple(map(int, input().split())) for _ in range(test_cases)]

    min_start = min([start for (start, end) in intervals])
    max_end = max([end for (start, end) in intervals])

    base_primes = simple_sieve(math.ceil(math.sqrt(max_end)))
    prime_numbers = segmented_sieve(base_primes, min_start, max_end)

    for (start, end) in intervals:
        interval_prime_numbers = []
        prime_number_index = 0

        for prime_number in prime_numbers:
            if prime_number < start:
                prime_number_index += 1
            else:
                break

        for _ in range(prime_number_index, len(prime_numbers)):
            if prime_numbers[prime_number_index] <= end:
                interval_prime_numbers.append(prime_numbers[prime_number_index])
                prime_number_index += 1
            else:
                break

        print("\n".join(map(str, interval_prime_numbers)))

run()
