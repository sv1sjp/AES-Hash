
from Crypto.Cipher import AES
from binascii import b2a_hex
import os,getpass

#XOR function
def XOR(word,key):
    xored = []
    for i in range(max(len(word), len(key))):
        xored_value = ord(word[i%len(word)]) ^ ord(key[i%len(key)])
        xored.append(hex(xored_value)[2:])
    return ''.join(xored)

#Make input strings multiple of 16 in length
def add_to_16(data):
 if len(data.encode('utf-8')) % 16:
  add = 16 - (len(data.encode('utf-8')) % 16)
 else:
  add = 0
 data = data + ('\0' * add)
 return data.encode('utf-8')


#  Encryption function 
def encrypt(data,key):
 bkey=key
 keysum=0
 i=0
 for index in bkey:
   
   keysum=keysum+ ord(bkey[i])
   i=i+1
   

 keysum=keysum+1000000000000000
 key = str(keysum)
 mode = AES.MODE_ECB
 data = add_to_16(data)
 cryptos = AES.new(key, mode)

 cipher_text = cryptos.encrypt(data)
 return b2a_hex(cipher_text)







if __name__ == '__main__':
 os.system('cls' if os.name == 'nt' else 'clear')
 print("_______________AES-hash by DimitrisV SV1SJP_______________")
 data=input("Give me a Plaintext: ")
 key = getpass.getpass(prompt='Give me a strong password: ')
 #key=input("Give me a strong password: ")
 xored_data=str(XOR(data,key))
 
 aes_enc = encrypt(xored_data,key) #  Encryption 
 aes_hashed=str(aes_enc)
 for character in key:
    aes_hashed= XOR(aes_hashed,key)
    aes_hashed= aes_hashed[4:68]
     
 print("\n ")
 

 print("___________________Your AES_hash:___________________ \n")    
 print(aes_hashed + "\n \n  GoodBye! :))")   

