#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 10:26:47 2020

@author: advaith
"""

#%%



# #LARGE PRIME OF BIT LENGTH CHOICE IS GENERATED
# def large_prime(bit_length):
#     # import time
#     # start_time = time.time()
#     from random import randrange, getrandbits
#     def is_prime(n, k=128):
#         """ Test if a number is prime
#             Args:
#                 n -- int -- the number to test
#                 k -- int -- the number of tests to do
#             return True if n is prime
#         """
#         # Test if n is not even.
#         # But care, 2 is prime !
#         if n == 2 or n == 3:
#             return True
#         if n <= 1 or n % 2 == 0:
#             return False
#         # find r and s
#         s = 0
#         r = n - 1
#         while r & 1 == 0:
#             s += 1
#             r //= 2
#         # do k tests
#         for _ in range(k):
#             a = randrange(2, n - 1)
#             x = pow(a, r, n)
#             if x != 1 and x != n - 1:
#                 j = 1
#                 while j < s and x != n - 1:
#                     x = pow(x, 2, n)
#                     if x == 1:
#                         return False
#                     j += 1
#                 if x != n - 1:
#                     return False
#         return True
#     def generate_prime_candidate(length):
#         """ Generate an odd integer randomly
#             Args:
#                 length -- int -- the length of the number to generate, in bits
#             return a integer
#         """
#         # generate random bits
#         p = getrandbits(length)
#         # apply a mask to set MSB and LSB to 1
#         p |= (1 << length - 1) | 1
#         return p
#     def generate_prime_number(length=bit_length):
#         """ Generate a prime
#             Args:
#                 length -- int -- length of the prime to generate, in  bits
#             return a prime
#         """
#         p = 4
#         # keep generating while the primality test fail
#         while not is_prime(p, 128):
#             p = generate_prime_candidate(length)
#         return p
#     ans_ = generate_prime_number()
#     # print(ans_)
#     return ans_
#     # import sympy as sy
#     # print(sy.isprime(ans_))
#     # print("--- %s seconds ---" % (time.time() - start_time))



    
# def gcd_(a,b): 
#     if(b==0): 
#         return a 
#     else: 
#         return gcd_(b,a%b)



# def rsa():
#     # import sympy as sy

#     bit_length = 4
#     p = large_prime(bit_length)
#     q = large_prime(bit_length)
#     while p == q:
#         q = large_prime(10)

#     n=p*q
#     print("p:",p)
#     print("q:",q)
#     print("n:",n)
#     n_1 = (p-1)*(q-1)
#     print("(p-1)(q-1):",n_1)
    
#     e = large_prime(bit_length+1)
#     while (gcd_(n_1,e)) != 1 and (e == p or e == q):
#         e = large_prime(bit_length)
#     print("e:",e)
    
#     d = 0
#     x = 0
#     while d == 0:
#         y = (n_1*x)+1
#         if y%e == 0:
#             d = int(y/e)
#         x = x+1
    
#     print("d:",d)
#     print(x)
    
#     print("PUBLIC KEY: ("+str(e)+", "+str(n)+")")
#     print("PRIVATE KEY: ("+str(d)+", "+str(n)+")")



# if __name__ == "__main__":
#     rsa()















#%%
    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 10:26:47 2020

@author: advaith
"""

""" NOTE: THIS IS VERSION 1 """

#%%


#%%

"""START OF MAIN CODE """
""" VERSION 1 """

# Large Prime Generation for RSA 
import random 

  
# Pre generated primes 
first_primes_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 
                     31, 37, 41, 43, 47, 53, 59, 61, 67,  
                     71, 73, 79, 83, 89, 97, 101, 103,  
                     107, 109, 113, 127, 131, 137, 139,  
                     149, 151, 157, 163, 167, 173, 179,  
                     181, 191, 193, 197, 199, 211, 223, 
                     227, 229, 233, 239, 241, 251, 257, 
                     263, 269, 271, 277, 281, 283, 293, 
                     307, 311, 313, 317, 331, 337, 347, 349] 
  
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
        for divisor in first_primes_list: 
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
    #n IS THE NUMBER OF BITS YOU WANT YOUR KEYS TO BE!! IMPORTANT!!
    #n CAN BE CHANGED IN MAIN
    
    
    
    p = get_prime(n)
    q = get_prime(n)
    while p == q:
        q = get_prime(n)

    n_=p*q
    # print("p:",p)
    # print("q:",q)
    # print("n:",n_)
    n_1 = (p-1)*(q-1)
    # print("(p-1)(q-1):",n_1)
    
    e = get_prime(n)
    while (gcd_(n_1,e)) != 1 or e == p or e == q:
        e = get_prime(n)
    # print("e:",e)
    
    # d = 0
    # x = 0
    # while d == 0:
    #     y = (n_1*x)+1
    #     if y%e == 0:
    #         d = int(y/e)
    #     x = x+1
    
    # print("d:",d)
    # print(x)
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
        # print("gcd(", a , "," , b, ") = ", g) 
        # print(x_,y_) 
        return x_
    
    d_ = gcdExtended(e,n_1)
    d = d_[1]
    if d < 0:
        d = d+n_1
    # print("d:",d)
    
    ## CHECK IF D IS CORRECT
    if ((d*e)-1)%n_1 != 0:
        print("your code for d (the private key is WRONG")
    
    
    # print("Length of public and private keys:")
    # print(len(str(e)))
    # print(len(str(d)))
    
    # print("\n")
    # print("Public and Private keys:\n")
    # print("PUBLIC KEY: ("+str(e)+", "+str(n_)+")\n")
    # print("PRIVATE KEY: ("+str(d)+", "+str(n_)+")")

    return e,d,n_

#We got the keys! Encryption time!

def encryption(e,d,n_,data):
    
    print("\n")
        
    #DATA TO BE ENCRYPTED

    # print("DATA:",data)
    # print("\n")
    # print("PUBLIC KEY: ("+str(e)+", "+str(n_)+")\n")
    # print("PRIVATE KEY: ("+str(d)+", "+str(n_)+")\n")

    ch = input ("Enter 1 to encode the data: ")
    if ch == "1":
        encoded_data = encryption_2(e,n_,data)
        print("Encoded:", encoded_data,"\n")
    else:
        pass    
    
    ch = input ("Enter 0 to decode the data: ")
    if ch == "0":
        decoded_data = encryption_2(d,n_,encoded_data)
        print("Decoded:", decoded_data,"\n")
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
                
    # print(len(e_b_list))
    l = len(e_b_list)-1
        
    for x in range(0,l+1):
        if x == 0:
            enc_t = data
        elif x == 1:
            enc_t = (data**(2**x))%n_
        else:
            enc_t = (enc_t*enc_t)%n_
    
        # print(enc_t)
        # print(e_b_list[l-x])
        if int(e_b_list[l-x]) == 1:
            temp_e = temp_e*enc_t
        # print(temp_e)
        
    encode = temp_e%n_
    # print(encode)
    print("\nTIME TO ENCODE AND DECODE: --- %s seconds ---" % (time.time() - start_time))
    return encode
    
    
def data_convert(data):
    # printing original list  
    # print("The original list : " + str(test_list)) 
    data_ = ""
    # Convert String list to ascii values 
    # using loop + ord() 
    res = [] 
    for ele in data: 
        res.extend(ord(num) for num in ele) 
      
    # printing result 
    # print("The ascii list is : " + str(res))
    
    for x in res:
        data_ = str(data_) + str(x)
        
    print(data_)
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
    n = 500
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
    
#%%

## ENCODING TRIAL
    
    
    
    
e=22733333
d=683
n_=26167


start_time = time.time()
encoded = data**e%n_     
print(encoded)
print("\nTIME TO ENCODE: --- %s seconds ---" % (time.time() - start_time))


start_time = time.time()
temp_e = 1
e_bin = "{0:b}".format(e)
d_bin = "{0:b}".format(d)

e_b_list = []
for x in str(e_bin):
    e_b_list.append(x)
    
d_b_list = []
for x in str(d_bin):
    d_b_list.append(x)

data = 3

# print(len(e_b_list))
l = len(e_b_list)-1
    
for x in range(0,l+1):
    if x == 0:
        enc_t = data
    elif x == 1:
        enc_t = (data**(2**x))%n_
    else:
        enc_t = (enc_t*enc_t)%n_

    # print(enc_t)
    # print(e_b_list[l-x])
    if int(e_b_list[l-x]) == 1:
        temp_e = temp_e*enc_t
    # print(temp_e)
    
encode = temp_e%n_
print(encode)
print("\nTIME TO ENCODE AND DECODE: --- %s seconds ---" % (time.time() - start_time))


    
#%%

## DATA COVERSION TO STRING AND THEN ASCII AND THEN CONCATENATE



data = "Hello World!"

# printing original list  
# print("The original list : " + str(test_list)) 
data_ = ""
# Convert String list to ascii values 
# using loop + ord() 
res = [] 
for ele in data: 
    res.extend(ord(num) for num in ele) 
  
# printing result 
# print("The ascii list is : " + str(res))

for x in res:
    data_ = str(data_) + str(x)
    
print(data_)




#%%



# printing original list  
# print("The original list : " + str(test_list)) 
data = 1010101010133

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

    

# data_ = ""
# # Convert String list to ascii values 
# # using loop + ord() 
# res = [] 
# for ele in data: 
#     res.extend(ord(num) for num in ele) 
      
#     # printing result 
#     # print("The ascii list is : " + str(res))
    
# for x in res:
#     data_ = str(data_) + str(x)
        
# print(data_)
# return data_























    
