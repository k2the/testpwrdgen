# pwrdGen.py - Basic password generator with 16 chatacters.
# Passwrod copied to clipboard & SHA256 hash digest is displayed

import random, pyperclip, hashlib

def pwrdGen():
    charcList = r'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[]^_`{|}~0123456789'
    recomdPwrdLength = 0
    genPwrd = ''
    
    while recomdPwrdLength != 16:
        mixUp = ''.join(random.sample(charcList,len(charcList)))
        ranNum = random.randint(0, len(mixUp)-1)
        randLetter = mixUp[ranNum]
        genPwrd += randLetter
        recomdPwrdLength +=1
        
    pyperclip.copy(genPwrd)
    print('Password copied to clipboard.')
    hashedPwrd = hashlib.sha256(str(genPwrd).encode('utf-8'))
    print('The SHA256 hash of the password is ' + hashedPwrd.hexdigest())

pwrdGen()


#TODO: regex for number,punctuation check?maybe repeating charac

'''
was going to use string module but couldnt figure out how to combine:
#charcLetters = string.ascii_letters
#charcNumbers = string.digits
#characPunct = string.punctuation
'''
