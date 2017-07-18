def next_palindrome(integer):
    pass


def run():
    test_cases = int(input())
    palindromes = '\n'.join(next_palindrome(input()) for _ in range(test_cases))
    print(palindromes)


run()