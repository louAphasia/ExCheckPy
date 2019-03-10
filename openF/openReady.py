the_file=open("ready.txt")
lines =the_file.readlines()
for line in lines:
    print(line)

the_file.close()