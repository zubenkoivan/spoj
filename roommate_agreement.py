import sys


def zero_sequences_count(sequence):
    curr_sum = 0
    sum_counts = {0: 1}
    result = 0
    for elem in sequence:
        curr_sum += elem
        curr_sum_count = sum_counts.get(curr_sum, 0)
        result += curr_sum_count
        sum_counts[curr_sum] = curr_sum_count + 1
    return str(result)


def run():
    sys.stdin.readline()
    lines = sys.stdin.readlines()
    lines = lines[1::2]
    sequences = map(lambda x: list(map(int, x.split())), lines)
    sys.stdout.write('\n'.join(map(zero_sequences_count, sequences)))


run()