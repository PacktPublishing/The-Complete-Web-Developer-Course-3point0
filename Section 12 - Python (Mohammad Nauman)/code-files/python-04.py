#! /usr/bin/python

print('Content-type: text/html')
print('')

print("Repeating Things <br />")

x = 0
while x <= 10:
    print(x)
    x += 1


for i in range(10):
    print(i, i*i)

for i in range(5, 10):
    print(i)


languages = ["Javascript", "PHP", "Python"]

for lang in languages:
    print("I know " + lang + ". <br />")


# Dictionary - 4 ssns (key) and names (value) of people
# Loop which prints. eg. ssn belongs to Hazel

ssns = {}
ssns["102-03"] = "Hazel"
ssns["890-23"] = "Christina"

print(ssns["102-03"])

for ssn in ssns:
    print(ssn + " belongs to " + ssns[ssn] + "<br />")

for ssn, person in ssns.items():
    print(ssn + " belongs to " + person + "<br />")
