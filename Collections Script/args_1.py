rec=[
    ('foo',1,2),
    ('bar','helli'),
    ('foo',3,4),
    ]

def dof(x,y):
    print('foo',x,y)

def dob(s):
    print('bar',s)

for tag, *args in rec:
    if tag=="foo":
        dof(*args)
    elif tag=='bar':
        dob(*args)