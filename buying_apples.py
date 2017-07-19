def min_money_amount(max_packets, kilograms, prices):
    for kg in range(2, kilograms + 1):
        for k in range(1, kg // 2 + 1):
            if prices[k] == -1 or prices[kg - k] == -1:
                continue
            if prices[kg] == -1:
                prices[kg] = prices[k] + prices[kg - k]
            else:
                prices[kg] = min(prices[kg], prices[k] + prices[kg - k])
    return prices[kilograms]


def read_test_case(row1, row2):
    max_packets, kilograms = [int(p) for p in row1.split()]
    prices = [0]
    prices.extend(int(p) for p in row2.split())
    return (max_packets, kilograms, prices)


def run():
    test_cases = int(input())
    amounts = [min_money_amount(*read_test_case(input(), input())) for _ in range(test_cases)]
    print('\n'.join(map(str, amounts)))


run()
