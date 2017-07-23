using System;
using System.Collections.Generic;

namespace alphacode
{
    class Program
    {
        static long[] PrefixCounts = new long[5001];

        static long DecodingsCount(string encryption)
        {
            for (int i = 1; i < encryption.Length; ++i)
            {
                int currCharCode = (int) encryption[i];
                int prevCharCode = (int) encryption[i - 1];
                int prefixLength = i + 1;

                if (currCharCode == 48)
                {
                    if (prevCharCode > 50 || prevCharCode == 48)
                    {
                        return 0;
                    }

                    PrefixCounts[prefixLength] = PrefixCounts[prefixLength - 2];
                }
                else 
                {
                    if (prevCharCode == 49
                        || (prevCharCode == 50 && currCharCode < 55))
                    {
                        PrefixCounts[prefixLength] = PrefixCounts[prefixLength - 1]
                                                     + PrefixCounts[prefixLength - 2];
                    }
                    else
                    {
                        PrefixCounts[prefixLength] = PrefixCounts[prefixLength - 1];
                    }
                }
            }

            return PrefixCounts[encryption.Length];
        }

        static void Main(string[] args)
        {
            PrefixCounts[0] = 1;
            PrefixCounts[1] = 1;

            var counts = new List<long>();

            while (true)
            {
                string encryption = Console.ReadLine();

                if (encryption == "0")
                {
                    break;
                }

                counts.Add(DecodingsCount(encryption));
            }

            foreach (long count in counts)
            {
                Console.WriteLine(count);
            }
        }
    }
}
