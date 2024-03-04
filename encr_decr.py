with open("msg.txt",'r')as file:
    content = file.read()
    print(f"\nThe content:- {content}")
    
#encrypt and decrypt using file handling

encrypted_data = ' '    
for word in content:
    encrypt = ord(word)
    encrypted_data += str(encrypt) + ' '
print(f"The encrypted result:- {encrypted_data}")

data_spliting = encrypted_data.split()

decrypted_data = ''
for txt in data_spliting:
    decrypt = chr(int(txt))
    decrypted_data += decrypt + ''
print(f"The decrypted result:- {decrypted_data}")

print("\n=================================================================================================")
    
#decrypting using file handling.

with open("msg_2.txt",'r')as file:
    content_2 = file.read()
    print(f"\nThe content:- {content_2}")
    
data_split = content_2.split()    
decrypted_content = ''
for text in data_split:
    decrypted = chr(int(text))
    decrypted_content += decrypted + ''
print(f"The decrypted result:- {decrypted_content}")