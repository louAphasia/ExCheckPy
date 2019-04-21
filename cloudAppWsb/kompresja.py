def LZW_encode(data):
    # krok. 1
    D = {}  # D - słownik: ciąg -> kod
    n = 0  # n - kod ciągu (liczba)
    for i in range(256):
        D[chr(i)] = n
        n = n + 1

    # krok 2.
    c = data[0]
    result = []

    # krok 3.
    for s in data[1:]:
        if c + s in D:
            # przypadek 1. (c+s w słowniku)
            c = c + s
        else:
            # przypadek 2.
            result.append(D[c])
            D[c + s] = n
            n = n + 1
            c = s

    # krok 4.
    result.append(D[c])

    # zwrócenie wyniku
    return result


def LZW_decode(data):
    # krok 1.
    D = {}  # D - słownik: kod -> ciąg
    n = 0  # n - kod ciągu (liczba)
    for i in range(256):
        D[n] = chr(i)
        n = n + 1

    # krok 2.
    pk = data[0]

    # krok 3.
    result = [D[pk]]

    # krok 4.
    for k in data[1:]:
        pc = D[pk]
        if k in D:
            # przypadek pierwszy: D[k] istnieje
            D[n] = pc + D[k][0]
            n = n + 1
            result.append(D[k])
        else:
            # przypadek specjalny: dekodowany jest
            # ciąg postaci scscs
            D[n] = pc + pc[0]
            n = n + 1
            result.append(pc + pc[0])
        pk = k

    return ''.join(result)


if __name__ == '__main__':
    import sys
    from math import log, ceil

    if len(sys.argv) < 2:
        print("Podaj nazwę pliku")
        sys.exit(1)

    data = open(sys.argv[1]).read()
    comp = LZW_encode(data)
    decomp = LZW_decode(comp)

    if data == decomp:
        k = len(comp)
        n = int(ceil(log(max(comp), 2.0)))

        l1 = len(data)
        l2 = (k * n + 7) / 8

        print("Liczba kodów: %d" % k)
        print("Maks. liczba bitów potrzebna do zapisania kodu: %d" % n)
        print("Rozmiar danych wejściowych: %d bajtów" % l1)
        print("Rozmiar danych skompresowanych: %d bajtów" % l2)
        print("Stopień kompresji: %.2f%%" % (100.0 * (l1 - l2) / l1))
    # print data
    # print decomp
    else:
        print("Wystąpił jakiś błąd!")