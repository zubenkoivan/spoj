def run():
    numbers = []

    while True:
        number = input()

        if number == '42':
            break

        numbers.primes(number)

        if len(numbers) == 500:
            print('\n'.join(numbers))
            numbers.clear()

    print('\n'.join(numbers))

run()
