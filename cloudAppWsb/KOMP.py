import math
import time

def buduj_slownika(tekst) -> str:
    slownik = sorted(set(tekst))
    return "".join(slownik)


def zworc_N(X) -> int:  # ilosc bitow na znak / przyjmuje dlugosc slownika
    return int(math.ceil(math.log(X) / math.log(2)))


def zworc_R(N, dlugosc) -> int:  # nadmiarowe bity
    return int((8 - (3 + N * dlugosc) % 8) % 8)


def dec_to_bin(liczba, N=None) -> str:  # zamienia znak na wartosc binarna i uzupelnia bity /
    # wyznacza ile bitow brakuje do potegi 8 /wyznacza 3 nadmiarowe bity

    binarna = ''  # wartosc binarna

    while liczba > 0:  # zamienia na binarne
        binarna = chr(48 + liczba % 2) + binarna
        # binarna += str(liczba % 2)
        liczba //= 2

    if N is None:
        while len(binarna) < 8:
            binarna = '0' + binarna
        return binarna

    for i in range(N):  # ilosc bitow na znak uzupeniona w przypadku 2 bitow na znak uzupelnia zerami do 2 bitow 1 -> 01
        if len(binarna) < N:
            binarna = '0' + binarna

    return binarna


def bin_to_dec(liczba) -> int:
    liczba = liczba[::-1]
    wynik = 0

    for i in range(len(liczba)):
        if liczba[i] == '1':
            wynik += 2 ** i
    return wynik


def kompresja(plik) -> str:
    slownik = buduj_slownika(plik)  # buduje slownik
    X = len(slownik)  # dlugosc slownika

    N = zworc_N(X)  # ilosc bitow na znak - 3 znaki na dwoch bitach 00 01 10
    R = zworc_R(N, len(plik))  # ilosc nadmiarowcyh bitow do dodania na koniec pliku

    skompresowany = [chr(X), slownik]  # X mowi ile bitow to slownik
    yield ''.join(skompresowany)
    # wylicza 3 nadmiarowe bity do dodania na koniec / te bity dodaje na poczatek
    tekst_binarny = dec_to_bin(R, 3)

    for i in plik:  # zamienia litery na wartosci binarne
        tekst_binarny += (dec_to_bin(slownik.index(i), N))  # dodaje binarne wartosci do poczatkowych bitow
        if len(tekst_binarny) >= 8:
            temp = tekst_binarny[:8]
            tekst_binarny = tekst_binarny[8:]
            # skompresowany.append(chr(bin_to_dec(temp)))
            yield chr(bin_to_dec(temp))

    # uzupelnia liczbe binarna nadmairowymi bitami
    if R > 0:
        for i in range(R):
            tekst_binarny += str('1')
        # skompresowany.append(chr(bin_to_dec(tekst_binarny)))
        yield chr(bin_to_dec(tekst_binarny))
    # return ''.join(skompresowany)


def dekompresja(plik_skompresowany) -> str:
    po_dekompresji = []

    # odczytanie dlogosci slownika
    X = ord(plik_skompresowany[0])

    # ilosc bitow na znak
    N = zworc_N(X)

    # odczytanie slownika
    slownik = plik_skompresowany[1:X + 1]

    # pierwszy znak skompresowanego tekstu (po slowniku)
    znak = dec_to_bin(ord(plik_skompresowany[X + 1]))

    # odcztanie nadmiarowych bitow z pierwzsego znaku
    bity = znak[:3]
    R = bin_to_dec(bity)  # nadmiarowe

    # pozostale bity
    bity = znak[3:8]

    temp = None
    # wczytuje pozostale bity (bez ostatniego)
    for i in range(X + 2, len(plik_skompresowany) - 1):
        znak = ord(plik_skompresowany[i])
        if znak < 0:
            znak = (znak + 256) % 256
        bity += dec_to_bin(znak)
        while len(bity) >= N:  # rozdzielenie bitow
            temp = bity[:N]
            index = bin_to_dec(temp)
            yield slownik[index]
            bity = bity[N:]

    # wczytywanie ostatniego znaku
    znak = ord(plik_skompresowany[len(plik_skompresowany) - 1])
    temp = dec_to_bin(znak)
    bity += temp[:8 - R]

    while len(bity) >= N:
        temp = bity[0:N]
        index = bin_to_dec(temp)
        yield slownik[index]
        bity = bity[N:]


def main():
    start = time.time()

    with open(r'D:\Pliki\testx.txt', 'r') as r:
        print("Kompresja pliku", r.name)
        with open(r'D:\Pliki\skompresowany.txt', 'w+', encoding='utf-8') as w:
            for i in kompresja(r.read()):
                w.write(i)

        print('Kompresja zakoczona')
        end = time.time()
        print('Czas wykonywania kompresji:', (end - start))
        start = time.time()
        print('Dekompresja...')

        with open(r'D:\Pliki\skompresowany.txt', 'r', encoding='utf-8') as r:
            with open(r'D:\Pliki\dekompresja.txt', 'w+') as w:
                for i in dekompresja(r.read()):
                    w.write(i)

    print('Dekompresja zakoczona')
    end = time.time()
    print('Czas wykonywania dekompresji:', (end - start))


if __name__ == '__main__':
    main()