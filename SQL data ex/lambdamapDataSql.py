listtuple=[('jan',35,'CEO'),('Ian',43,'account')]

m=[age for(name,age,job) in listtuple]

n=list(map((lambda row:row[1]),listtuple))

print(m)
print(n)