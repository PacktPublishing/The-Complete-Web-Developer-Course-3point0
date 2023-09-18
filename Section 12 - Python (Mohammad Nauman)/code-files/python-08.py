#! /usr/bin/python

import requests
print('Content-type: text/html')
print('')


response = requests.get('https://catfact.ninja/fact')
print(response.text)    # print raw text
print('<br />')

print(response.json())  # get a dictionary like format
print('<br />')

response = response.json()
print(response['fact'])  # extract individual data pieces from the response


# Some free APIs to try. Change data extarction field above based on the API's response
# https://catfact.ninja/fact
# https://randomuser.me/api/
# http://universities.hipolabs.com/search?country=United+States
# https://api.github.com/events
