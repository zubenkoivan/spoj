using System;
using System.Collections.Generic;
using System.Linq;

namespace acronymmaker
{
    class AcronymsCounter
    {
        private const int MaxWords = 51;
        private const int MaxAcronymLength = 75;

        private static long[][] PrefixCounts = new long[MaxWords][];
        private static string[] Words = new string[MaxWords];
        private static int[] MaxAcronymIndexes = new int[MaxWords];

        static AcronymsCounter()
        {
            for (int i = 0; i < PrefixCounts.Length; ++i)
            {
                PrefixCounts[i] = new long[MaxAcronymLength];
            }
        }

        private readonly string _acronym;
        private readonly int _wordsCount;

        public AcronymsCounter(HashSet<string> insignificantWords, string[] words)
        {
            _acronym = words[0].ToLower();
            _wordsCount = InitWords(insignificantWords, words);
            PrefixCounts[0][0] = 1L;

            for (int i = 1; i <= _wordsCount; ++i)
            {
                MaxAcronymIndexes[i] = _acronym.Length - _wordsCount + i;
            }
        }

        private int InitWords(HashSet<string> insignificantWords, string[] words)
        {
            int count = 0;

            for (int i = 1; i < words.Length; ++i)
            {
                if (insignificantWords.Contains(words[i]))
                {
                    continue;
                }

                if (count == MaxWords)
                {
                    return -1;
                }

                count += 1;
                Words[count] = words[i];
            }

            return count;
        }

        private void Reset()
        {
            for (int i = 0; i <= _wordsCount; ++i)
            {
                Array.Clear(PrefixCounts[i], 0, _acronym.Length + 1);
            }
        }

        public long Count()
        {
            int maxSymbolsPerWord = _acronym.Length - _wordsCount + 1;

            if (_wordsCount <= 0 || maxSymbolsPerWord < 1)
            {
                return 0;
            }

            for (int w = 1; w <= _wordsCount; ++w)
            {
                int maxAcronymIndex = w > 1 ? (w - 1 + maxSymbolsPerWord) : 1;

                for (int a = w - 1; a < maxAcronymIndex; ++a)
                {
                    FillPrefixCounts(w, 0, 0, a);
                }
            }

            long count = PrefixCounts[_wordsCount][_acronym.Length];

            Reset();

            return count;
        }

        private void FillPrefixCounts(int word, int wordMatchedCount, int wordIndex, int acronymIndex)
        {
            string word_str = Words[word];
            int wordLength = word_str.Length;
            int maxAcronymIndex = MaxAcronymIndexes[word];

            for (int i = wordIndex; i < wordLength; ++i)
            {
                if (word_str[i] != _acronym[acronymIndex])
                {
                    continue;
                }

                long count = PrefixCounts[word - 1][acronymIndex - wordMatchedCount];

                PrefixCounts[word][acronymIndex + 1] += count;

                if (i + 1 < wordLength)
                {
                    FillPrefixCounts(word, wordMatchedCount, i + 1, acronymIndex);
                }

                wordMatchedCount += 1;
                acronymIndex += 1;

                if (acronymIndex == maxAcronymIndex)
                {
                    break;
                }
            }
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            foreach (var testCase in ReadTestCases().ToList())
            {
                string acronym = testCase.Item2[0];
                var acronymsCounter = new AcronymsCounter(testCase.Item1, testCase.Item2);
                long acronymsCount = acronymsCounter.Count();

                PrintAcronymsCount(acronym, acronymsCount);
            }
        }

        static IEnumerable<Tuple<HashSet<string>, string[]>> ReadTestCases()
        {
            while (true)
            {
                int n = int.Parse(Console.ReadLine());

                if (n == 0)
                {
                    break;
                }

                var insignificantWords = new HashSet<string>();

                for (int i = 0; i < n; ++i)
                {
                    insignificantWords.Add(Console.ReadLine());
                }

                while (true)
                {
                    string line = Console.ReadLine();

                    if (line == "LAST CASE")
                    {
                        break;
                    }

                    yield return new Tuple<HashSet<string>, string[]>(insignificantWords, line.Split());
                }
            }
        }

        static void PrintAcronymsCount(string acronym, long count)
        {
            if (count == 0L)
            {
                Console.WriteLine(acronym + " is not a valid abbreviation");
            }
            else
            {
                Console.WriteLine(acronym + $" can be formed in {count.ToString()} ways");
            }
        }
    }
}
