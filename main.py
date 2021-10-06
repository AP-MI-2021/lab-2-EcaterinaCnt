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

def get_base_2(n: str) -> str:
    '''
    Transformă un număr dat din baza 10 în baza 2. Numărul se dă în baza 10.
    :param n: numar in baza 10
    :return: numar in baza 2
    '''
    resturi_n =[]
    x=0
    while n != 0:
        resturi_n.append(n % 2)
        n=n //2
    lungime = len(resturi_n)
    for i in range (lungime-1, -1, -1):
        x= x*10 + resturi_n[i]
    return x

def test_get_base_2():
    assert get_base_2(123) == 1111011
    assert get_base_2(75) == 1001011

def main():
    while True:
        print ("7. Determină dacă un număr este antipalindrom")
        print(("11. Afișează toți anii bisecți între doi ani dați (inclusiv anii dați)"))
        print("8.Transformă un număr dat din baza 10 în baza 2")
        print("x. Iesire din porogram")
        optiune = input("Alegeti optiunea: ")
        if optiune == "7":
            n = int(input("Cititi numarul: "))
            print(is_antipalindrome(n))
        elif optiune == "11":
            n = int(input("Cititi anul: "))
            print(get_leap_years(n))
        elif optiune == "8":
            n = int(input("Cititi numarul: "))
            print(get_base_2(n))
        elif optiune =="x":
            break
        else:
            print("Optiune invalida.")
test_get_leap_years()
test_is_antipalindrome()
test_get_base_2()
if __name__ == "__main__":
    main()

