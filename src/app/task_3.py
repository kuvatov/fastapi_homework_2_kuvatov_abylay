def convert_to_american_standart(numbers: int) -> str:
    numbers_list = list(str(numbers))
    
    for i in range(len(numbers_list) - 3, 0, -3):
        numbers_list.insert(i, ',')

    return ''.join(numbers_list)


if __name__ == '__main__':
    print('Sample Input:')
    numbers = int(input('> '))
    result = convert_to_american_standart(numbers)
    print('*' * 20)
    print('Sample Output:')
    print('> ' + result)
    