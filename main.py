def get_leap_years(start: int, end: int) -> list[int]:
    '''
    -Determina anii bisecti
    Input:
    -anul de inceput, anul de final, numere intregi, naturale
    Output:
    - Anii bisecti
    '''
    years_list = []
    i = start
    for i in range(i, end + 1):
        if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
            years_list.append(i)

    return years_list


def test_get_leap_years():
    assert get_leap_years(2000, 2021) == [2000, 2004, 2008, 2012, 2016, 2020]
    assert get_leap_years(1990, 2001) == [1992, 1996, 2000]

test_get_leap_years()