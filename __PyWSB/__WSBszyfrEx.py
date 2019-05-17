print('First module name is {}'.format(__name__))

if __name__=="__main__":
   cipher={'a':'o','e':'i'}
   cipherdev={cipher[v]: v for v in cipher.keys()}
   print(cipherdev)


   is_running=True
   while is_running:
     print('aaa')
     x=input()
     if x=='exit':
        is_running=False



