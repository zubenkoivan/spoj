def distance(stalls, start, end):
    return stalls[end] - stalls[start]


def check(c, min_distance, stalls):
    extra_stalls = len(stalls) - c
    prev_stall = 0

    for c_left in range(c - 1, 1, -1):
        next_stall = prev_stall + 1
        current_distance = distance(stalls, prev_stall, next_stall)

        while extra_stalls > 0 and current_distance < min_distance:
            extra_stalls -= 1
            next_stall += 1
            current_distance = distance(stalls, prev_stall, next_stall)

        if current_distance < min_distance:
            return False

        prev_stall = next_stall

    return distance(stalls, prev_stall, -1) >= min_distance


def find_min_distance(c, stalls):
    low = 0
    high = distance(stalls, 0, -1) // (c - 1)

    while low < high:
        mid = low + (high - low - 1) // 2 + 1

        if check(c, mid, stalls):
            low = mid
        else:
            high = mid - 1

    return low


def run():
    test_cases = int(input())
    input_stream = map(lambda x: tuple(map(int, input().split())), range(test_cases))
    input_stream = map(lambda x: (x[1], list(int(input()) for _ in range(x[0]))), input_stream)

    for (c, stalls) in input_stream:
        stalls.sort()
        print(find_min_distance(c, stalls))


run()
