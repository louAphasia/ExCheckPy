from numpy import average, sum

data = ['ACME', 50, 90.1, (2012, 7, 23)]
name, age, price, date = data

print(date)

grade = (2, 3, 4, 5, 6)


def drop_first_lat(grade):
    first, *middle, last = grade
    return average(middle)


print(drop_first_lat(grade))

s = [10, 1, 5, 3]


def countA(a):
    *dane,current=a
    data_avg = sum(dane)/len(dane)
    return (data_avg/current)


print(countA(s))
