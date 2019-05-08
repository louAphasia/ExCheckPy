import ciag_arytmetyczny

a = int(input("podaj pierwszy wyraz ciagu "))
r = int(input("podaj roznice "))

n = int(input("Podaj n-ty wyraz ciagu "))
wynik = ciag_arytmetyczny.funkcja(a, r, n)
print("n-ty wyraz twojego ciagu ", wynik)

print("suma n-tych wyrazow ", (((a + wynik)/2)*n))
