##password generator

import random
import string
password = []

def lc():
    password.append(random.choice(string.ascii_lowercase))
def uc():
    password.append(random.choice(string.ascii_uppercase))
def pn():
    password.append(random.choice(string.punctuation))
def dg():
    password.append(random.choice(string.digits))

limit = random.randrange(7,14)
def pick():
    i = 0
    lc()
    uc()
    pn()
    dg()
    
    while i < limit:
        pk = random.choice("abcd")
        if pk == "a":
            lc()
        elif pk == "b":
            uc()
        elif pk == "c":
            pn()
        elif pk == "d":
            dg()
        i += 1



pick()
random.shuffle(password)
print("".join(password))




