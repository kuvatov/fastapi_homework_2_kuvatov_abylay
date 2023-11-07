def reverse_last_five_numbers(numbers: int) -> str:
    numbers = str(numbers)
    last_five_numbers = numbers[-5:]
    reversed_numbers = last_five_numbers[::-1]
    remains = numbers[:-5]

    if len(numbers) <= 5:
        return reversed_numbers
    return remains + reversed_numbers


if __name__ == '__main__':
    print('Sample Input:')
    numbers = int(input('> '))
    result = reverse_last_five_numbers(numbers)
    print('*' * 20)
    print('Sample Output:')
    print('> ' + result)
