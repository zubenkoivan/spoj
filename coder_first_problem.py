def f(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    if x == 2:
        return 2
    if x & 1 == 1:
        return 0
    return 2 * trailing_zeros_count(x)


def trailing_zeros_count(value):
    zeros_count = 1
    if value & 0xffff == 0:
        zeros_count += 16
        value = value >> 16
    if value & 0xff == 0:
        zeros_count += 8
        value = value >> 8
    if value & 0xf == 0:
        zeros_count += 4
        value = value >> 4
    if value & 3 == 0:
        zeros_count += 2
        value = value >> 2
    zeros_count -= value & 1
    return zeros_count


def run():
    x = int(input())
    print(f(x))


run()