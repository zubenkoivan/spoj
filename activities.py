import sys


counts = [0 for _ in range(100001)]


def solve(classes):
    classes = sorted(classes, reverse=True)
    total = len(classes)
    for i in range(0, len(classes)):
        curr_class = classes[i]
        start = binary_search(curr_class[1], classes)
        count = counts[start] + counts[i] + 1
        counts[i + 1] = count % 100000000
    return '%08d' % (counts[len(classes)])


def binary_search(min_class_start, classes):
    start = 0
    end = len(classes)
    while start < end:
        mid = (start + end) >> 1
        class_start = classes[mid][0]
        if min_class_start > class_start:
            end = mid
        else:
            start = mid + 1
    return end


def get_classes(lines):
    count = 0
    classes = None
    for line in lines:
        if count == 0:
            count = int(line)
            classes = []
            continue
        curr_class = line.split()
        classes.append((int(curr_class[0]), int(curr_class[1])))
        count -= 1
        if count == 0:
            yield classes


def run():
    results = map(solve, get_classes(sys.stdin.readlines()))
    sys.stdout.write('\n'.join(results))


run()
