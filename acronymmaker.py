import itertools


def acronym_count(insign_words, line):
    acronym, words = split_words(insign_words, line)
    max_symbols_per_word = len(acronym) - len(words) + 1
    if max_symbols_per_word < 1:
        return (acronym.upper(), 0)
    acc_words_lens = get_acc_words_lens(words)
    prefix_counts = [[0] * (len(acronym) + 1) for _ in range(len(words) + 1)]
    prefix_counts[0][0] = 1
    words = ''.join(words)
    test_case = (prefix_counts, acc_words_lens, acronym, words)
    for word in range(1, len(prefix_counts)):
        max_acronym_idx = (word - 1 + max_symbols_per_word) if word > 1 else 1
        for acronym_idx in range(word - 1, max_acronym_idx):
            fill_prefix_counts(test_case, (word, acc_words_lens[word - 1], 0, acronym_idx))
    return (acronym.upper(), prefix_counts[-1][-1])


def fill_prefix_counts(test_case, state):
    prefix_counts, acc_words_lens, acronym, words = test_case
    word, words_idx, word_matched_len, acronym_idx = state
    if words_idx == acc_words_lens[word] or acronym_idx == len(acronym):
        return
    max_acronym_idx = len(acronym) - (len(prefix_counts) - 1 - word)
    for i in range(words_idx, acc_words_lens[word]):
        if words[i] == acronym[acronym_idx]:
            count = prefix_counts[word - 1][acronym_idx - word_matched_len]
            prefix_counts[word][acronym_idx + 1] += count

            fork_state = (word, i + 1, word_matched_len, acronym_idx)
            fill_prefix_counts(test_case, fork_state)

            word_matched_len += 1
            acronym_idx += 1

            if acronym_idx == max_acronym_idx:
                break


def split_words(insign_words, line):
    words = line.split()
    acronym = words[0].lower()
    words = itertools.islice(words, 1, len(words))
    words = list(filter(lambda x: insign_words.get(x) is None, words))
    return (acronym, words)


def get_acc_words_lens(words):
    lens = [0]
    lens.extend(map(len, words))
    for i in range(1, len(lens)):
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
