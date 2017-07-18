def operation_priorities():
    return {
        '+': 0,
        '-': 1,
        '*': 2,
        '/': 3,
        '^': 4
    }


def process_operator(curr_operator, operators, priorities):
    rpn = ''
    prev_operator = operators.pop() if len(operators) > 0 else None

    while prev_operator is not None \
          and priorities[prev_operator] >= priorities[curr_operator]:
        rpn += prev_operator
        prev_operator = operators.pop() if len(operators) > 0 else None

    if prev_operator is not None:
        operators.append(prev_operator)

    operators.append(curr_operator)

    return rpn


def to_rpn(expression, start=0):
    priorities = operation_priorities()
    operators = []
    rpn = ''
    i = start

    if expression[i] == '(':
        i += 1

    while i < len(expression):
        symbol = expression[i]

        if symbol == '(':
            inner_rpn_length, inner_rpn = to_rpn(expression, i)
            i += inner_rpn_length
            rpn += inner_rpn
        elif symbol == ')':
            i += 1
            break
        elif symbol.isalpha():
            rpn += symbol
            i += 1
        else:
            rpn += process_operator(symbol, operators, priorities)
            i += 1

    rpn += ''.join(reversed(operators))

    return (i - start, rpn)

def run():
    test_cases = int(input())
    expressions = [input() for _ in range(test_cases)]
    print('\n'.join(map(lambda x: to_rpn(x)[1], expressions)))


run()
