import random
import math

def is_prime(x):
  if x < 2:
    return False
  for i in range(2, int(x ** 0.5) + 1):
    if x % i == 0:
      return False
  return True

def random_prime(start, end):
  while True:
    number = random.randint(start, end)
    if is_prime(number):
      return number
def generate_public_private(a, b):
  c = a * b
  d = (a - 1) * (b - 1)
  #find number where gcd of d and e is 1
  e = None
  for i in range(2, d):
    if is_prime(i) == False:
      continue
    if math.gcd(d, i) == 1:
      e = i
      break
  
  print("Created public key pair")
  
  f = None
  for i in range(2, d):
    if(i * e) % d == 1:
      f = i
      break
  print("Created private key pair")
  return c, e, f


a = random_prime(50, 200)
b = random_prime(50, 200)

c, public, private = generate_public_private(a, b)

print("c: {}, public: {}, private: {}".format(c, public, private))
  
def encrypt(randomNumber, e, c):
  return pow(randomNumber, e) % c

def decrypt(crypted, f, c):
  return pow(crypted, f) % c

randomText = random.randint(100, 1000)
encrypted = encrypt(randomText, public, c)
decrypted = decrypt(encrypted, private, c)

print("Plain Text: {}, encrypted: {}, decrypted: {}".format(randomText, encrypted, decrypted))
  
  
  
  