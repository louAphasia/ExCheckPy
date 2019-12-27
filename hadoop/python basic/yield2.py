                 #  # generator-version
def makeRange(n):                #  def makeRange(n):
    """return [0,1,2,...,n-1]""" #~     """return 0,1,2,...,n-1"""
    TO_RETURN = []               #>
    i = 0                        #      i = 0
    while i < n:                 #      while i < n:
        TO_RETURN += [i]         #~         yield i
        i += 1                   #          i += 1  ## indented
    return TO_RETURN             #>


def makeR(n):
    i=0
    while i<n:
        yield i
        i+=1

for i in makeR(5):
    print(i)

def fib():
    last, cur =0,1
    while True:
        yield cur
        last, cur = cur, last+cur

print(fib())
print(fib().__next__())
print(fib().__next__())
print(fib().__next__())
print(fib().__next__())
print(fib().__next__())
print(fib().__next__())
print(fib().__next__())
