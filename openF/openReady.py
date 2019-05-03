the_file=open("ready.txt")
lines =the_file.readlines()
for line in lines:
    print(line)

the_file.close()

fh=open('ready.txt','rb')
while True:
    wiersz=fh.read()
    if len(wiersz)==0:break
    print(wiersz)
fh.close()