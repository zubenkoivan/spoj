import itertools


def right_gte_left(integer):
    right_start = len(integer) // 2
    for i in range(right_start, len(integer)):
        left = int(integer[len(integer) - i - 1])
        right = int(integer[i])
        if right > left:
            return True
        elif right < left:
            return False
    return True


def mirror_left(integer):
    left_end = (len(integer) - 1) // 2
    left = itertools.islice(integer, 0, left_end + 1)
    right_start = len(integer) // 2 + (len(integer) & 1)
    right = itertools.islice(reversed(integer), right_start, None)
    return ''.join(itertools.chain(left, right))


def increment_left(integer):
    middle = (len(integer) - 1) // 2
    left = list(integer[middle::-1])
    carry = 1
    for i in range(len(left)):
        if left[i] == '9':
            left[i] = '0'
        else:
            left[i] = str(int(left[i]) + 1)
            carry = 0
            break
    return (carry, left)

def mirror_incremented_left(integer):
    carry, left = increment_left(integer)
    if carry == 1:
        left.append('1')
        if len(integer) & 1 == 0:
            left_str = ''.join(left)
            return left_str[:0:-1] + left_str
        else:
            left_str = ''.join(left[1:])
            return left_str[::-1] + left_str
    left_str = ''.join(left)
    if len(integer) & 1 == 0:
        return left_str[::-1] + left_str
    return left_str[:0:-1] + left_str


def next_palindrome(integer):
    integer = integer if len(integer) == 1 else integer.lstrip('0')
    if right_gte_left(integer):
        return mirror_incremented_left(integer)
    return mirror_left(integer)


def run():
    test_cases = int(input())
    palindromes = '\n'.join(next_palindrome(input())
                            for _ in range(test_cases))
    print(palindromes)


run()