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

def is_antipalindrome(n) -> bool:
    cifre_n = []
    while n > 0:
        cifre_n.append(n % 10)
        n = n // 10

    lenght=len(cifre_n)
    '''
    i=0
    while i<=lenght//2:
        if cifre_n[i] == cifre_n[lenght-1-i]:
            return False
        i=i+1
'''
    for i in range(0,lenght//2):
          if cifre_n[i] == cifre_n[lenght-1-i]:
              return False

    return True
def test_is_antipalindrome():
    assert is_antipalindrome(2783) == True
    assert is_antipalindrome(2773) == False

test_get_leap_years()
test_is_antipalindrome()