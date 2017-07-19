import itertools


def acronym_count(insign_words, line):
    acronym, words = split_words(insign_words, line)
    acc_words_lens = get_acc_words_lens(words)
    prefix_counts = [[0 for _ in range(len(acronym) + 1)]
                     for _ in range(len(words) + 1)]
    words = ''.join(words)
    test_case = (prefix_counts, acc_words_lens, acronym, words)
    fill_prefix_counts(test_case, (1, 0, 0, 0))
    return prefix_counts[-1][-1]


def fill_prefix_counts(test_case, state):
    prefix_counts, acc_words_lens, acronym, words = test_case
    word, words_idx, word_acronym_len, acronym_idx = state
    for i in range(words_idx, acc_words_lens[word]):
        if words[i] == acronym[acronym_idx]:
            fork_state = (word, i + 1, word_acronym_len, acronym_idx)
            fill_prefix_counts(test_case, fork_state)


def split_words(insign_words, line):
    words = line.split()
    acronym = words[0].lower()
    words = itertools.islice(words, 1, len(words))
    words = [filter(lambda x: insign_words[x] is not None, words)]
    return (acronym, words)


def get_acc_words_lens(words):
    lens = [0].extend(map(len, words))
    for i in range(1, len(words)):
        lens[i] += lens[i - 1]
    return lens


def acronym_count_str(acronym, count):
    if count == 0:
        return acronym + ' is not a valid abbreviation'
    return acronym + ' can be formed in %d ways' % count


def read_test_cases():
    while True:
        words_count = int(input())
        if words_count == 0:
            break
        insignificant_words = {}
        for _ in range(words_count):
            insignificant_words[input()] = True
        while True:
            line = input()
            if line == 'LAST CASE':
                break
            yield (insignificant_words, line)


def run():
    acronyms_counts = map(lambda x: acronym_count(*x), read_test_cases())

    print('\n'.join(map(lambda x: acronym_count_str(*x), acronyms_counts)))


run()