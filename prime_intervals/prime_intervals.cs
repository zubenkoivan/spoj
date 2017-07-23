using System;

namespace prime_intervals
{
    class Program
    {
        public static int ReadInt(string line)
        {
            return int.Parse(line);
        }

        public static long[] ReadLong(string line, int count)
        {
            string[] numbers = line.Split(' ');
            var result = new long[count];

            for (int i = 0; i < numbers.Length; ++i)
            {
                result[i] = long.Parse(numbers[i]);
            }

            return result;
        }

        static void Main(string[] args)
        {
            Run();
        }

        private const long Max = 2147483647;
        private const int Limit = 46341;
        private const int LimitPrimeNumbersCount = 4791;

        private static readonly int[] FlagsBuffer = new int[(1000000 >> 6) + 1];
        private static readonly StringBuilder PrintBuffer = new StringBuilder(1000);

        public static void Run()
        {
            int testCasesCount = ReadInt(Console.ReadLine());

            if (testCasesCount == 0)
            {
                return;
            }

            int[] basePrimeNumbers = SimpleSieve();

            for (int i = 0; i < testCasesCount; ++i)
            {
                long[] row = ReadLong(Console.ReadLine(), 2);
                long start = row[0];
                long end = row[1];
                int firstNumber = (int) start;
                int lastNumber = end == Max ? (int) Max - 1 : (int) end;

                if ((firstNumber & 1) == 0)
                {
                    ++firstNumber;
                }

                if ((lastNumber & 1) == 0 || end == Max)
                {
                    --lastNumber;
                }

                int[] flags = SegmentedSieve(basePrimeNumbers, firstNumber, lastNumber);
                PrintPrimeNumbers(flags, start, end, firstNumber, lastNumber);
            }
        }

        private static int[] SegmentedSieve(int[] primeNumbers, int firstNumber, int lastNumber)
        {
            int intervalLength = lastNumber - firstNumber + 1;
            int[] isNotPrime = FlagsBuffer;

            Array.Clear(isNotPrime, 0, (intervalLength >> 6) + 1);

            for (int i = 0; i < primeNumbers.Length; ++i)
            {
                int primeNumber = primeNumbers[i];
                int firstMultiple = primeNumber * primeNumber;

                if (firstMultiple > lastNumber)
                {
                    break;
                }

                if (firstMultiple < firstNumber)
                {
                    firstMultiple = ((firstNumber - 1) / primeNumber + 1) * primeNumber;

                    if ((firstMultiple & 1) == 0)
                    {
                        firstMultiple += primeNumber;
                    }
                }

                int step = primeNumber << 1;

                for (long multiple = firstMultiple; multiple <= lastNumber; multiple += step)
                {
                    SetTrue(isNotPrime, (int) (multiple - firstNumber));
                }
            }

            return isNotPrime;
        }

        private static int[] SimpleSieve()
        {
            int limit = (int) Math.Ceiling(Math.Sqrt(Limit));
            var isNotPrime = FlagsBuffer;
            var primeNumbers = new int[LimitPrimeNumbersCount];
            int index = 0;

            for (int number = 3; number <= Limit; number += 2)
            {
                if (IsTrue(isNotPrime, number))
                {
                    continue;
                }

                primeNumbers[index] = number;
                ++index;

                if (number > limit)
                {
                    continue;
                }

                int step = number << 1;

                for (int multiple = number * number; multiple <= Limit; multiple += step)
                {
                    SetTrue(isNotPrime, multiple);
                }
            }

            return primeNumbers;
        }

        private static void PrintPrimeNumbers(int[] isNotPrime,
            long start, long end,
            int firstNumber, int lastNumber)
        {
            if (start == 2)
            {
                PrintBuffer.Append(2);
                PrintBuffer.Append(Environment.NewLine);
            }

            for (int number = firstNumber; number <= lastNumber; number += 2)
            {
                if (IsTrue(isNotPrime, number - firstNumber))
                {
                    continue;
                }

                PrintBuffer.Append(number);
                PrintBuffer.Append(Environment.NewLine);

                if (PrintBuffer.Length > 980)
                {
                    Console.Write(PrintBuffer.ToString());
                    PrintBuffer.Clear();
                }
            }

            if (PrintBuffer.Length > 0)
            {
                Console.Write(PrintBuffer.ToString());
                PrintBuffer.Clear();
            }

            if (end == Max)
            {
                Console.WriteLine(Max);
            }
        }

        private static bool IsTrue(int[] flags, int number)
        {
            int mask = 1 << ((number >> 1) & 31);

            return (flags[number >> 6] & mask) == mask;
        }

        private static void SetTrue(int[] flags, int number)
        {
            int mask = 1 << ((number >> 1) & 31);
            int index = number >> 6;

            flags[index] |= mask;
        }
    }
}
