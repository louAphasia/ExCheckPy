def cezar(strin):
    n=13
    alpha="AĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻ"
    alpham=alpha.lower()
    result=''

    for litera in strin:
        if litera in alpha:
            oldi=alpha.index(litera)
            newi=(oldi+n)%len(alpha)
            result += alpha[newi]
        elif litera in alpham:
            oldi=alpham.index(litera)
            newi=(oldi+n)%len(alpham)
            result+=alpham[newi]
        else :
            result +=litera
    return result


def __sprawdz(jawny, oczekiwany):
    otrzymany = cezar(jawny)
    assert otrzymany == oczekiwany, 'Tekst "{}" po zaszyfrowaniu to "{}", Twoja funkcja zwróciła "{}".'.format(jawny, oczekiwany, otrzymany)

tekst_jawny = 'ala'
oczekiwany_szyfr = 'kwk'

__sprawdz(tekst_jawny, oczekiwany_szyfr)
print('Sprawdzenie poprawności rozwiązania... Test 2/4...')
tekst_jawny = 'Ala'
oczekiwany_szyfr = 'Kwk'
__sprawdz(tekst_jawny, oczekiwany_szyfr)
print('Sprawdzenie poprawności rozwiązania... Test 3/4...')
tekst_jawny = 'Ala.'
oczekiwany_szyfr = 'Kwk.'
__sprawdz(tekst_jawny, oczekiwany_szyfr)
print('Sprawdzenie poprawności rozwiązania... Test 4/4...')
tekst_jawny = 'Ala ma kota i psa.'
oczekiwany_szyfr = 'Kwk zk uaek ś bćk.'
__sprawdz(tekst_jawny, oczekiwany_szyfr)
print("Rozwiązanie poprawne.")