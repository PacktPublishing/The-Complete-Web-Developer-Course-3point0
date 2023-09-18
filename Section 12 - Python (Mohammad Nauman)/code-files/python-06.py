#! /usr/bin/python

print('Content-type: text/html')
print('')


print("Something <br />")


def log():
    print("Info!")


log()


def log(msg):
    print(msg + "<br />")


log("Using functions to make our life easy")


def log(msg, tag):
    print(tag + ":" + msg + "<br />")


log("Using functions to make our life easy", "error")


def log(msg):
    print(msg + "<br />")


log("Fix The Prime Code from Earlier")


def isPrime(num):
    for divisor in range(2, num):
        if num % divisor == 0:
            return False

    return True


for num in range(2, 100):
    if (isPrime(num)):
        print(num)
