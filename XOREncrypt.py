def encrypt(plaintext, k):
    answer = []
    for index, value in enumerate(plaintext):
        byte_answer = []
        byte_plaintext = ''.join(format(i, '08b') for i in bytearray(value, encoding ='utf-8'))
        byte_k = ''.join(format(i, '08b') for i in bytearray(k[index], encoding ='utf-8'))
        for i in range(len(byte_k)):
            if byte_plaintext[i] == byte_k[i]:
                byte_answer.append('0')
            else:
                byte_answer.append('1')
        answer.append(chr(int(''.join(byte_answer), 2)))
    return ''.join(answer)

print(encrypt('hello', 'noway'))
