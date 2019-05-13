from bs4 import BeautifulSoup
import requests


'''r=requests.get('http://mpk.wroc.pl/kontrole-biletow').text


#print(r)

soup=BeautifulSoup(r,'html.parser')
ss=soup.select_one('span[class="date-display-single"]')
print("Możliwe dzisiaj kontrole " , str(ss.string).strip())
datetab=soup.find_all("span class","date")
routestab=soup.find_all("td", class_="views-field views-field-title")

parsed_d=[]
parsed_r=[]

for r in routestab:
    parsed_r.append((str(r.string).strip()))

for d in datetab:
    parsed_d.append((str(d.string).strip()))

for k,v in zip(parsed_d,parsed_r):
    print(k + '-'+ v)'''


from datetime import date

# pobieramy kod HTML strony (tak jak jest to w przykładzie z dokumentacji biblioteki requests)
html = requests.get('http://mpk.wroc.pl/kontrole-biletow').text

# wykorzystujemy bibliotekę Beautiful Soup do sparsowania strony (zamiany kodu HTML na obiekty Pythona)
soup = BeautifulSoup(html, 'html.parser')

# znajduję wszystkie wiersze znajdujące się na stronie
# tak się składa, że są to tylko wiersze tabeli z informacją o kontrolach
all_rows = soup.find_all('tr')

# wybieramy wszystkie wiersze oprócz pierwszego (w pierwszym wierszu znajdują się nagłówki)
rows_without_heading = all_rows[1:]

 # tworzę trzy zmienne do przechowywania informacji
#  o kontrolach przed dniem dzisiejszym, dziś
# i w dniach kolejnych
before = []  # lista krotek (dzień, ulica, linia)
current = ()
after = []

# w tej zmiennej przechowuję aktualną datę
today = date.today()

# pętla for przechodzi przez każdy wiersz
# i wpisuje znalezione informacje do odpowiedniej zmiennej
for row in rows_without_heading:   #ta zmienna przechowuje komórki z danego wiersza
    cells = row.find_all('td')

# na podstawie komórki 0 tworzona jest lista
#zawierająca dzień miesiąc i rok - funkcja split
# rozdziela napis na listę według podanego napisu
    day_month_year_in_row = cells[0].text.split('.')
# tworzony jest obiekt typu date na podstawie wcześniejszej listy
    date_in_row = date(int(day_month_year_in_row[2]),
                int(day_month_year_in_row[1]),
                int(day_month_year_in_row[0]))

# porównujemy daty i dodajemy odpowiednie krotki do zmiennych
    if date_in_row < today:
            before.append((cells[0].text.strip(), cells[1].text.strip(), cells[2].text.strip()))
    if date_in_row == today:
            current = (cells[0].text.strip(), cells[1].text.strip(), cells[2].text.strip())
    if date_in_row > today:
            after.append((cells[0].text.strip(), cells[1].text.strip(), cells[2].text.strip()))

# wypisujemy zebrane informacje
line = "Możliwe konrole dzisiaj: " + current[2] + " (" + current[1] + ")"
print(line)
print("^" * len(line))

print("Przewidywane kontrole w kolejnych dniach:")
for c in after:
    print(" * " + c[0] + ": " + c[2])

print("Ostatnie kontrole:")
for c in before:
    print(" * " + c[0] + ": " + c[2])