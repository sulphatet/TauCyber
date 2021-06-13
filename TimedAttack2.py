
import time
import sys # ignore
sys.path.insert(0,'.') # ignore
from Root.pswd import real_password

def check_password(password): # Don't change it
    if len(password) != len(real_password):
        return False
    for x, y in zip(password, real_password):
        time.sleep(0.1) # Simulates the wait time of the safe's mechanism
        if int(x) != int(y):
            return False
    return True

def crack_password():
    password = [0,0,0,0]
    crack = ''

    for i in range(4):
        for j in range(10):
            password[i] = j
            start = time.time()
            check_password(password)
            end = time.time()
            if(i == 3):
                if(check_password(password)):
                    crack += str(j)
                    break
            elif(end - start >= 0.2 + i/10):
                crack += str(j)
                break

    return(crack)

print(crack_password)
