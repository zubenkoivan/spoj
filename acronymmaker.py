class AcronymCounter:
    max_words = 51
    prefix_counts = [[0] * 75 for _ in range(max_words)]
    words = [''] * max_words
    max_acronym_indexes = [0] * max_words


    def __init__(self, insignificant_words, all_words):
        self._acronym = all_words[0].lower()
        self._words_count = self.__init_words(insignificant_words, all_words)
        self.prefix_counts[0][0] = 1
        for i in range(1, self._words_count + 1):
            self.max_acronym_indexes[i] = len(self._acronym) - self._words_count + i


    def __init_words(self, insignificant_words, all_words):
        count = 0
        for i in range(1, len(all_words)):
            if insignificant_words.get(all_words[i]) is not None:
                continue
            if count == self.max_words:
                return -1
            count += 1
            self.words[count] = all_words[i]
        return count


    def __reset(self):
        for i in range(self._words_count + 1):
            for j in range(len(self._acronym) + 1):
                self.prefix_counts[i][j] = 0


    def count(self):
        max_symbols_per_word = len(self._acronym) - self._words_count + 1
        if self._words_count <= 0 or max_symbols_per_word < 1:
            return 0
        for w in range(1, self._words_count + 1):
            max_acronym_idx = (w - 1 + max_symbols_per_word) if w > 1 else 1
            for a in range(w - 1, max_acronym_idx):
                self.__fill_prefix_counts(w, 0, 0, a)
        count = self.prefix_counts[self._words_count][len(self._acronym)]
        self.__reset()
        return count


    def __fill_prefix_counts(self, word, word_matched_len, word_idx, acronym_idx):
        word_str = self.words[word]
        word_len = len(word_str)
        max_acronym_idx = self.max_acronym_indexes[word]
        for i in range(word_idx, word_len):
            if word_str[i] != self._acronym[acronym_idx]:
                continue
            count = self.prefix_counts[word - 1][acronym_idx - word_matched_len]
            self.prefix_counts[word][acronym_idx + 1] += count

            if i + 1 < word_len:
                self.__fill_prefix_counts(word, word_matched_len, i + 1, acronym_idx)

            word_matched_len += 1
            acronym_idx += 1

            if acronym_idx == max_acronym_idx:
                break


def print_acronym_count(acronym, count):
    if count == 0:
        print(acronym + ' is not a valid abbreviation')
    else:
        print(acronym + ' can be formed in %d ways' % count)


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
            yield (insignificant_words, line.split())


def run():
    acronyms_counts = []
    for test_case in read_test_cases():
        acronym = test_case[1][0]
        counter = AcronymCounter(*test_case)
        acronyms_counts.append((acronym, counter.count()))
    for count in acronyms_counts:
        print_acronym_count(*count)


run()
