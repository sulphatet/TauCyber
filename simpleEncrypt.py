def encrypt(plaintext, k):
   result = ""
   # transverse the plain text
   for i in range(len(plaintext)):
        char = plaintext[i]
        result += chr((ord(char) + (k - 97) % 26 + 97)
   return result
   
print(encrypt)
