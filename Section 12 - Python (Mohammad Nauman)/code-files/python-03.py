#! /usr/bin/python

print('Content-type: text/html')
print('')

# this is the usual header

# We have basic numbers (integers)
age = 22
print(age)
print('<br />')  # this is just to make the browser happy

pi = 3.1415
print(pi)
print('<br />')

name = "Hazel"
print(name)
print('<br />')

# We can also print results of expressions
print(age + 5)
print('<br />')

# Sometimes, expressions yield unexpected results ...
# (these actually have good reasons)

number = "5"
print(number * 3)      # no error but did you expect the result?
# print(number * pi)   # this is an error
print('<br />')


# We can change types of data using "casting"
print(float(number) * pi)
print('<br />')

str = "My Name Is "

print("Full string: " + str + '<br />')


print("0th character: " + str[0] + '<br />')
print("0-4 characters: " + str[0:5] + '<br />')
print("4th character: " + str[5] + '<br />')

print(str + name)
print('<br />')

# Lists are very useful structures used everywhere
# ... contact list, message list, social media feeds
print('Working with Lists ... <br />')
myList = ["Hazel", "Christina", "May", "Ralphie"]

print(myList)
print('<br />')

# Just as we did with strings, we can get individual elements from a list using indexing
print(myList[0])
print('<br />')

print(myList[1:4])
print('<br />')

# We can add stuff to lists
myList.append("John")
print(myList)
print('<br />')

# Tuples are very similar to lists except we can't change them
# ... they're more efficient and make your code better. No need to worry about how at the moment.
print('Working with tuples ... <br />')

# Notice the difference in brackets
myTuple = ("Hazel", "Christina", "May", "Ralphie")

print(myTuple)
print('<br />')

print(myTuple[1])
print('<br />')

# myTuple.append("John")   # Error
print(myTuple)
print('<br />')

# Sometimes it's difficult to get invidual records from list
# .. that's when dictionaries come in handy

print('Working with dictionaries ... <br />')
ssns = {}
ssns["102-03"] = "Hazel"
ssns["890-23"] = "Christina"

print(ssns)
print('<br />')

print(ssns["102-03"])
print('<br />')


