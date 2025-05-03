# Scraping and parsing HTMl data usinf BeautifulSoup library
import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup
import ssl
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE
url = input("Enter the url: ")  

try:
    fhand = urllib.request.urlopen(url,context=ctx).read()
    soup = BeautifulSoup(fhand, 'html.parser')

    # Retrieving all the anchor tags from the web page
    tags = soup('a')
    for tag in tags:
        href = tag.get('href', None)
        if href:  # Check if href exists (is not None)
            print(href)
except urllib.error.URLError as e:
    print(f"Error opening URL: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
print("Afshan Qasim")
