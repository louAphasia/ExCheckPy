x=open('file').readlines()  #readlines() zwraca znak konca /n
print(x)

y=[line.rstrip().strip('-') for line in open('file').readlines()]
print(y)

z=list(map((lambda line: line.rstrip()),open('file').readlines()))
print(z)