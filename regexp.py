import re


text="Korem dolor ipsem lorum sorem agromas dolor suus sorem"
find=re.search("dolor.*sorem",text)

print(find)

print(type(find))

print(find.start(), find.end(), find.group())

findlist=list(re.finditer("dolor",text))
print(findlist)

print(bool(re.match("[0-9]*","0ggfd78")))

y=re.sub("dolor.*sorem","suus",text)
print(y)

def getNrOcc(string,sub):
    find=list(re.finditer(sub,string))
    print(find)
    return len(find)

print(getNrOcc("ala ma wiele kotow ala ala", r'al.'))