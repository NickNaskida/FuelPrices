import requests
from pprint import pprint

from bs4 import BeautifulSoup

URL = 'https://www.sgp.ge/ge/price'
HEADERS = {
	'agent': 'Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) \
		Chrome/52.0.2743.98 Mobile Safari/537.36'
}


def parse_socar_data():
	response = requests.get(URL, headers=HEADERS)
	soup = BeautifulSoup(response.content, 'html.parser')
	title_items = soup.find_all('th')[1:]
	price_items = soup.find_all('tr')[1].find_all('td')[1:]

	data = {}

	title_items[3].string.replace_with("ევრო რეგულარი")
	title_items[5].string.replace_with("ევრო დიზელი")

	for i, j in zip(title_items, price_items):
		data.update({i.get_text(strip=True): j.get_text(strip=True)})

	return data


if __name__ == "__main__":
	pprint(parse_socar_data())
