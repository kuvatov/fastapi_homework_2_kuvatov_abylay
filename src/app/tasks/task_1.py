def str_sum(text: str) -> tuple[int, int]:
    symbol = 60
    ruble = len(text) * symbol // 100
    kopeck = len(text) * symbol % 100

    return ruble, kopeck


if __name__ == '__main__':
    print('Sample Input:')
    user_input = input('> ')
    result = str_sum(user_input)
    print('*' * 20)
    print('Sample Output:')
    print('> ' + f'{result[0]} р., {result[1]} коп.')
    