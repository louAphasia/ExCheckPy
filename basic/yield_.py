def gen(n):
 for i in n:
     yield i*2

def square(x):
    for i in range(x):
        yield i**2
        # wysyla obiekt z powrotem do wywolujacego ZAPAMIETUJE gdzie skonczyl dzialani

print(list(square(10)))


