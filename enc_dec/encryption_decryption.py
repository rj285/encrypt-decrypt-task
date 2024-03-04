#=====Encrypting and Decrypting using File Handlig=====

print("\n=====|TASK-1|FILE HANDLING -- ENCRYPT & DECRYPT|=====") #printing the mentiond text

with open("msg.txt",'+r')as file: #opening the file and giving permission to 'read'
    content = file.read() #reads and stores the file content into 'content'
    print(f"\n\tThe content :- {content}") #printing the content from the file

encrypted_content = ' ' #empty string to store encrypted data
for txt in content: #iterate each data from content to i
    encr = ord(txt) - 96 #make the character to corresponding numeric value by substract ascii value of each character
    encrypted_content += str(encr) + ' ' #adding the 'encr' to 'encrypted_content' by using str(covert numbers to string)
print(f"\nThe Encrypted result:- {encrypted_content}") #printing the encrypted result

splited_data = encrypted_content.split() #splitting the 'encrypted_content' into list and stores in 'splited_data'
descrypted_content = ' ' #empty string to store decrypted data
for con in splited_data: #iterate each data from splited_data to con
    desc = chr(int(con) + 96) #descrypte by adding that encrypted character with +96 and convert that numerics to character by using chr function
    descrypted_content += desc  #adding the 'desc' to 'descrypted_content' 
print(f"\nThe descripted result:- {descrypted_content}") #printing the decrypted result


#=====Encrypting data using file handling=====

with open("to_encrypt.txt",'+r')as file: #opening the file and giving permission to 'read'
    to_encrypt = file.read() #reads and stores the file content into 'to_encrypt'
    print(f"\nText to Encrypt:- {to_encrypt}") #printing the content from the file
print(f"\nThe Encrypted result:-") #printing the mentiond text
for i in to_encrypt: #iterate each data from to_encrypt to i
    small_case = i.lower() #converts data from 'i' to small case 
    encrypt = ord(small_case) - 96 #make the character to corresponding numeric value by substract ascii value of each character
    print(encrypt,end=" ") #printing the encrypted result
    
    
#=====Decrypting data using file handling=====    
    
with open("to_decrypt.txt",'+r')as file: #opening the file and giving permission to 'read'
    to_decrypt = file.read() #reads and stores the file content into 'to_decrypt'
    print(f"\nText to Decrypt:- {to_decrypt}") #printing the content from the file
print(f"\nThe Decrypted result:-") #printing the mentiond text

splited_text = to_decrypt.split() #splitting the 'to_decrypt' into list and stores in 'splited_text'
# print(splited_text)
for j in splited_text: #iterate each data from splited_text to j
    decrypt = chr(int(j) + 96) #descrypte by adding that encrypted character with +96 and convert that numerics to character by using chr function
    print(decrypt,end=" ") #printing the decrypted result
    
    
    



