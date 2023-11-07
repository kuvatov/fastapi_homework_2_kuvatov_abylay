ZODIAC = ['дракон', 'змея', 'лошадь', 'овца', 'обезьяна', 'петух', 'собака', 'свинья', 'крыса', 'бык', 'тигр', 'заяц']
CYCLE = 12


def get_zodiac_by_year(year: int) -> str:
    # Значение -8 берётся для коррекции индекса из списка, чтобы индексы находились в пределах от -8 до 3
    return ZODIAC[year % CYCLE-8].capitalize()


if __name__ == '__main__':
    print('Sample Input:')
    year = int(input('> '))
    result = get_zodiac_by_year(year)
    print('*' * 20)
    print('Sample Output:')
    print('> ' + result)
