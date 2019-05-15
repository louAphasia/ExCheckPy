
import random, sys, os, cloudAppWsb.RSA.CryptoMATH


def main():

    print('Make files')
    makeKeyFiles('nadisnowdi',1024)
    print("Key files made.")

    generatorKey(1024)

def generatorKey(keySize):
    p=0
    q=0
    #Step 1 PRIMES p i q
    while p==q:
        p= generateLargePrime(keySize)
        q= PRIMESNum.generateLargePrime(keySize)

    n=p*q

    #step 2 create e

    print("generating e prime relative to p-1(q-1)")
    while True:
        e=random.randrange(2**(keySize-1),2**(keySize))
        if CryptoMATH.gcd(e, (p - 1) * (q - 1))==1:
            break

    # step 3 the mod inverse of e
    print ("Generating d mod inverse of e" )
    d= CryptoMATH.findModInverse(e, (p - 1) * (q - 1))

    publicKey=(n,e)
    privateKey=(n,d)
    print(publicKey,'ccc', privateKey)

    return (publicKey,privateKey)

def makeKeyFiles(name,keySize):

    if os.path.exists('%s_pubkey.txt'%(name)) or os.path.exists('%s_private.txt'%(name)):
            sys.exit('WARNING: THE FILE %s_pubkey.txt or %s_privatekey.txt already exists!use diffrent name or delete'% (name,name))

    publicKey, privateKey=generatorKey(keySize)

    print()
    print('thr public key is a %s and a %s digit nr' % (len(str(publicKey[0])),(len(str(publicKey[1])))))
    print('writing public key to file %s_publickey.txt...'%(name))
    fo=open('%s_publickey.txt' % (name), 'w')
    fo.write('%s,%s,%s'% (keySize,privateKey[0], publicKey[1]))
    fo.close()


if __name__=='__main__':
        main()



