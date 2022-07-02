import requests
from pprint import pprint

from bs4 import BeautifulSoup

URL = 'http://www.lukoil.ge/'
HEADERS = {
	'agent': 'Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) \
		Chrome/52.0.2743.98 Mobile Safari/537.36'
}


def parse_lukoil_data():
	response = requests.get(URL, headers=HEADERS)
	soup = BeautifulSoup(response.content, 'html.parser')
	items = soup.find_all('div', class_="price-card")

	data = {}

	for i in items:
		data.update({i.find_all('h3')[0].get_text(strip=True): i.find_all('h3')[1].get_text(strip=True)})

	return data


if __name__ == "__main__":
	pprint(parse_lukoil_data())
