
def mapper(line):
    userId, movieId ,rating = line.split(",")
    if rating == "rating":
        yield
    result = [rating, 1]
    yield result

def reducer(self, key, value):
    result = [key,float(key) * sum(float(value))/ sum(value)]
    yield result


lis = " 1, ala, 32 "



for x in mapper(lis):
    print(x)