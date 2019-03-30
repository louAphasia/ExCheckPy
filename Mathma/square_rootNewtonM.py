
def square_r(n):
    root=n/2
    for k in range(20):
        root=(1/2)*(root+(n/root))
        print(root)
    return root

print(square_r(9))

print(square_r(16))