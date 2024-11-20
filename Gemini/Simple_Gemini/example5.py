from bs4 import BeautifulSoup
import requests

# Make a request to the webpage
response = requests.get('https://www.zerogpt.com')
soup = BeautifulSoup(response.text, 'html.parser')

# Find the textarea and set its value
text_area = soup.select_one('textarea#textArea.textarea.notresizable')
# Note: For scraping, you typically can't change the page content; you'd need JavaScript for that.

# Find the percentage span
percentage_span = soup.select_one('span.header-text.text-center')
percentage_text = percentage_span.text

print('Percentage:', percentage_text)
