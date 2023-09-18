#! /usr/bin/python

print('Content-type: text/html')
print('')

num = 24

if num == 1 or num == 0:
    print("Number is indeed 0 or 1!")
else:
    print("Number is not zero or one")

print(num % 2)
if num % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")


print("Finding primes between 1 and 1,000 <br />")


for num in range(2, 1000):
    isPrime = True

    for divisor in range(2, num):
        if num % divisor == 0:
            isPrime = False

    if isPrime == True:
        print(num)


# 983 is a prime!
