#%%
    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 10:26:47 2020

@author: advaith
"""

""" NOTE: THIS IS VERSION 2 """


#%%

"""START OF MAIN CODE """
""" VERSION 2 """

# Large Prime Generation for RSA 
import random 
import math as m

  
# Pre generated primes 
def pre_prime():
    ch = 0
    prime = []
    prime.append(2)
    for n in range(3,350,2):        
        x = m.sqrt(n)
        for i in range(len(prime)):
            if prime[i] <= x: 
                if n%prime[i] == 0:
                    ch = 1
            if ch == 1:
                break
        if ch == 0:
            prime.append(n)
        ch = 0
    return prime

  
def nBitRandom(n): 
    return random.randrange(2**(n-1)+1, 2**n - 1) 
  
def getLowLevelPrime(n): 
    '''Generate a prime candidate divisible  
    by first primes'''
    while True: 
        # Obtain a random number 
        pc = nBitRandom(n)  
  
         # Test divisibility by pre-generated  
         # primes 
        primes_list = pre_prime()
        for divisor in primes_list: 
            if pc % divisor == 0 and divisor**2 <= pc: 
                break
        else: return pc 
  
def isMillerRabinPassed(mrc): 
    '''Run 20 iterations of Rabin Miller Primality test'''
    maxDivisionsByTwo = 0
    ec = mrc-1
    while ec % 2 == 0: 
        ec >>= 1
        maxDivisionsByTwo += 1
    assert(2**maxDivisionsByTwo * ec == mrc-1) 
  
    def trialComposite(round_tester): 
        if pow(round_tester, ec, mrc) == 1: 
            return False
        for i in range(maxDivisionsByTwo): 
            if pow(round_tester, 2**i * ec, mrc) == mrc-1: 
                return False
        return True
  
    # Set number of trials here 
    numberOfRabinTrials = 20 
    for i in range(numberOfRabinTrials): 
        round_tester = random.randrange(2, mrc) 
        if trialComposite(round_tester): 
            return False
    return True
  
def get_prime(n):
    while True: 
        prime_candidate = getLowLevelPrime(n) 
        if not isMillerRabinPassed(prime_candidate): 
            continue
        else: 
#            print(n, "bit prime is: \n", prime_candidate)
            return prime_candidate
            break



    
def gcd_(a,b): 
    if(b==0): 
        return a 
    else: 
        return gcd_(b,a%b)



def rsa(n):    
    p = get_prime(n)
    q = get_prime(n)
    while p == q:
        q = get_prime(n)

    n_=p*q
    n_1 = (p-1)*(q-1)
    e = get_prime(n)
    while (gcd_(n_1,e)) != 1 or e == p or e == q:
        e = get_prime(n)
    def gcdExtended(a, b):  
    # Base Case  
        if a == 0 :   
            return b,0,1                 
        gcd,x1,y1 = gcdExtended(b%a, a)  
        # Update x and y using results of recursive  
        # call  
        x_ = y1 - (b//a) * x1  
        y_ = x1  
         
        return gcd,x_,y_ 
        # Driver code 
        g, x, y = gcdExtended(a, b)  
        return x_
    
    d_ = gcdExtended(e,n_1)
    d = d_[1]
    if d < 0:
        d = d+n_1

    return e,d,n_

#We got the keys! Encryption time!

def encryption(e,d,n_,data):
    
    print("\n")
        
    #DATA TO BE ENCRYPTED
    ch = input ("Enter 1 to encode the data: ")
    if ch == "1":
        encoded_data = encryption_2(e,n_,data)
        print("Encoded:", encoded_data,"\n")
        print("PUBLIC KEY USED: ("+str(e)+", "+str(n_)+")\n")
    else:
        pass    
    
    ch = input ("Enter 0 to decode the data: ")
    if ch == "0":
        decoded_data = encryption_2(d,n_,encoded_data)
        print("Decoded:", decoded_data,"\n")
        print("PRIVATE KEY USED: ("+str(d)+", "+str(n_)+")")
    else:
        pass
        
    return encoded_data, decoded_data
    
    
    
def encryption_2(e,n_,data):
    start_time = time.time()
    temp_e = 1
    e_bin = "{0:b}".format(e)

    e_b_list = []
    for x in str(e_bin):
        e_b_list.append(x)
                
    l = len(e_b_list)-1
        
    for x in range(0,l+1):
        if x == 0:
            enc_t = data
        elif x == 1:
            enc_t = (data**(2**x))%n_
        else:
            enc_t = (enc_t*enc_t)%n_
    
        if int(e_b_list[l-x]) == 1:
            temp_e = temp_e*enc_t        
    encode = temp_e%n_
    print("\nTIME TO ENCODE AND DECODE: --- %s seconds ---" % (time.time() - start_time))
    return encode
    
    
def data_convert(data):
    data_ = ""
    # Convert String list to ascii values 
    # using loop + ord() 
    res = [] 
    for ele in data: 
        res.extend(ord(num) for num in ele) 
    for x in res:
        data_ = str(data_) + str(x)
        
    # print(data_)
    return data_



def data_convert_back(data):
    if isinstance(data, int):
        data = str(data)
        x=0
        z=""
        while x<len(data):
            y=str(data[x])
            # print(y)
            while int(y)<32 or int(y)>127:
                x+=1
                y=str(y)+str(data[x])
            z=str(z)+chr(int(y))
            x+=1
        print(z)

if __name__ == "__main__":
    n = 1024
    import time
    e,d, n_ = rsa(n)   
    data = input ("Enter a string: ")
    # print(data)
    data_int = int(data_convert(str(data)))
    enc, dec = encryption(e,d,n_,data_int)
    
    ch_ = input("Convert decoded data back to string? (y to continue): ")
    if ch_ == "y":
        data_convert_back(dec)
    else:
        pass
    print("\nEnd of program. \n\n")
    
    
"""END OF MAIN CODE"""