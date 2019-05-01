func=[lambda x: x**2,lambda x:x*3]

###########
def makea():
    acts=[]
    for i in range(5):
        acts.append(lambda x,i=i:i**x)  # nie moze byc (lambda x,i:x**i) musi byc i=i
    return acts

acts=makea()
print(acts[4](2))
###############

lower=(lambda x,y: x if x<y else y)
print(lower('bbb','aaa'))

action=(lambda x:(lambda y: x+y))

act=action(10)
print(act(3))

print(((lambda x:(lambda y: x+y))(10))(3))