cipher = {'a': 'y', 'e': 'i', 'i': 'o', 'o': 'a', 'y': 'e'}


def encode(plaintext,cipher) -> str:
#    cipher = {'a': 'y', 'e': 'i', 'i': 'o', 'o': 'a', 'y': 'e'}

    for ch in plaintext:
        if ch in cipher.keys():
           plaintext=plaintext.replace(ch,cipher.get(ch))

    return (plaintext)

def decode(encoded):

    cipherrev={'y':'a','i':'e','o':'i','a':'o','e':'y'}
    for i in encoded:
        if i in cipherrev.keys():
            encoded=encoded.replace(i,cipherrev.get(i))
    return (encoded)

def decoded(szyfr,dic):
    pass





'''#Convert each letter of plaintext to the corrsponding
	#encrypted letter in our dictionary creating the cryptext
	ciphertext=""
	for l in plaintext:
		if l in dic:
			l=dic[l]
		ciphertext+=l
	for i in alphabet:
		print i,
	print
	for i in key:
		print i,
	print
	return ciphertext,key


# This function decodes the ciphertext using the key and creating
# the reverse of the dictionary created in substitution to retrieve
# the plaintext again
def decode(alphabet,ciphertext,key):
	
	dic={}
	for i in range(0,len(key)):
		dic[key[i]]=alphabet[i]

	plaintext=""
	for l in ciphertext:
		if l in dic:
			l=dic[l]
		plaintext+=l

	return plaintext'''







'''def decode(secret, encoding_cipher):
    decode_cipher = {value: key for key, value in encoding_cipher.items()}
    return encode(secret, decode_cipher)'''


def main():


    plaintext = "hello foo"
    print(encode(plaintext,cipher))

    print(decode(encode(plaintext)))

if __name__ == '__main__':
    main()
