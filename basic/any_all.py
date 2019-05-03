def avoids(word,forbidden):
    return not any(letter in forbidden for letter in word)

a=['ala','pies','kot','mysz']

print(avoids('kot',a))