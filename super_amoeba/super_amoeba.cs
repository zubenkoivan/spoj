using System;

namespace super_amoeba
{
    class Program
    {
        static void Main(string[] args)
        {
            int testCases = int.Parse(Console.ReadLine());

            for (int i = 0; i < testCases; ++i)
            {
                string[] line = Console.ReadLine().Split();
                int m = int.Parse(line[0]);
                int n = int.Parse(line[1]);
                Console.WriteLine(FindAmoeba(m, n));
            }
        }

        static string FindAmoeba(int m, int n)
        {
            const int c = 1000000007;
            long y = PowMod(m, n, c);
            long x = (Mod(y - 1, c) * Mod(ModInverse(m - 1, c), c)) % c;

            return $"{x.ToString()} {y.ToString()}";
        }

        static long PowMod(int a, int e, int c)
        {
            long b = a % c;
            long result = 1;

            while (e > 0)
            {
                if ((e & 1) == 1)
                {
                    result = (result * b) % c;
                }

                e >>= 1;
                b = (b * b) % c;
            }

            return result;
        }

        static long ModInverse(int a, int c)
        {
            int r0 = c;
            int r1 = a;
            long t0 = 0;
            long t1 = 1;

            while (r1 > 0)
            {
                int q = r0 / r1;
                int rTmp = r0 - q * r1;
                r0 = r1;
                r1 = rTmp;
                long tTmp = t0 - q * t1;
                t0 = t1;
                t1 = tTmp;
            }

            return t0;
        }

        static long Mod(long a, int c)
        {
            long remainder = a % c;
            return remainder < 0 ? (remainder + c) : remainder;
        }
    }
}
