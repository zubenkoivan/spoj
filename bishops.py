import sys


def bishops_count(n):
    return '1' if n == 1 else str(2 * n - 2)

def run():
    board_sizes = map(int, sys.stdin.readlines())
    bishops_counts = map(bishops_count, board_sizes)
    sys.stdout.write('\n'.join(bishops_counts))


run()
