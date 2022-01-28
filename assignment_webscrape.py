from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import numpy as np

# ignore ssl certificate errors (for https)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# read html data
# (urls to try:)
# http://py4e-data.dr-chuck.net/comments_42.html
# http://py4e-data.dr-chuck.net/comments_1474130.html
url = input('Enter URL: ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# initialize array to store comment counts
comment_counts = []

# retrieve span tags
tags = soup('span')
for tag in tags:
	comment_counts.append(int(tag.contents[0]))

# print sum of all comment counts
print('Number of tags: ' + str(len(comment_counts)))
print('Sum is: ' + str(np.sum(comment_counts)))
