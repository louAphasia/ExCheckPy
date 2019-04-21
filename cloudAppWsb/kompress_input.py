

def kompress(data):
    list=[]   # krok. 1
    #D = {}  # D - słownik: ciąg -> kod

    for i in range(256):
       #D[i] = 0
       list.append(0)

    x=len(data)
    for i in range(x):
      list[i]=1

    print(list)











if __name__ == '__main__':



  kompress("aaabbbccc")
