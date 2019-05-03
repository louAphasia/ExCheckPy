mess="nadi jest malutka malusienka a snowdi bardzo duza"

count={}

for ch in mess:
    count.setdefault(ch,0)
    count[ch]=count[ch]+1

print(count)

spam={2:'33',1:"34"}
spam.setdefault(25,"234")  # jesli nie ma to wpisz a jesli jest to key to wypisz value w dict
print(spam)

print(spam.setdefault(1))

###
picnicItems={'apples':5,'ctron':5}
print('i m '+ str(picnicItems.get('apples',0))+'apples')
print('i m '+ str(picnicItems.get('eggs',4))+'eggs')  #sprawdza czy jest eggs jak nie ma wpisuje 4 a jakby bylo picnicItems['eggs'] bylby blad
print(picnicItems)