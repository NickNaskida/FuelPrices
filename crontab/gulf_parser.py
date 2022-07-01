import requests
from pprint import pprint

from bs4 import BeautifulSoup

URL = 'https://gulf.ge/'
HEADERS = {
	'agent': 'Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) \
		Chrome/52.0.2743.98 Mobile Safari/537.36'
}


def parse_data():
	response = requests.get(URL, headers=HEADERS)
	soup = BeautifulSoup(response.content, 'html.parser')
	items = soup.find_all('div', class_='price_entry')

	data = {}

	for i in items:
		data.update({i.find('div', class_='product_name').get_text(strip=True): i.find('div', class_='product_price').get_text(strip=True)})

	return data


if __name__ == "__main__":
	pprint(parse_data())
