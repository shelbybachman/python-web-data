# this program takes a URL
# (use URLs below)
# extracts all anchor tags,
# follows the link at the Xth position on the page
# and repeats the process a specified number of times,
# printing out the URL to follow each time


import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# get html data
# URLs to try:
# http://py4e-data.dr-chuck.net/known_by_Fikret.html
# http://py4e-data.dr-chuck.net/known_by_Melica.html
url = input('Enter URL: ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# initialize empty list of names
names = []

# retrieve all anchor tags
# and get href= values
tags = soup('a')

# set position of interest
# for each page, this picks the X'th link and follows it
position = 18

# number of times to repeat the process
n_times = 7

# include URL from position 1
names.append(tags[0].get('href', None))
print(tags[0].get('href', None))

# function to find link at position X, follow link
def find_follow_third_link(url,position_number):
        # follow the url
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup('a')  
        # return the next url to follow
        return tags[position_number-1].get('href',None)

for i in range(n_times):
	if i == 0:
		url = tags[position-1].get('href', None)
		names.append(url)
		print(url)	
	# also pull name
	if i > 0:
		url = find_follow_third_link(url,position)
		names.append(url)
		print(url)
