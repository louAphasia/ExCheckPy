print(bin(1980))
slices='albsterkot'

print(slices[1:9:2])


name="Kate"

s=name[2].rjust(2)
print(s)

w=name.lower()
print(w)

kod_t=1
kod_r=20
# konwersja z powrotem na stringi
kod_napis = '%02d-%03d' % (kod_t, kod_r)
print(kod_napis)