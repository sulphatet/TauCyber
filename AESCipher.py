from Crypto.Cipher import AES
from Crypto import Random
import itertools
import sys # ignore
sys.path.insert(0,'.') # ignore
from Root.prev_func import aes_decrypt, is_english

def brute_force_aes(ciphertext):
    for x in range (1,999999):
        number = '036' + str(x).zfill(6) + '0000000'
        number = number.encode() #turn to 8 bit
        plainnum = aes_decrypt(ciphertext,number)
        if is_english(plainnum):
            return(plainnum, number)
