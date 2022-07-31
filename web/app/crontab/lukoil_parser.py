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
	items = soup.find_all('div', class_="mt-4 w-full h-2/5 flex justify-center items-center text-xl text-lk-main flex-col")

	data = {}
	data_values = []
	data_keys = ["სუპერ ეკტო", "პრემიუმ ავანგარდი", "ევრო რეგულარი", "ევრო დიზელი"]

	for i in items[0:]:
		data_values.append(i.find_all('p')[0].get_text(strip=True))

	for name, price in zip(data_keys, data_values[1:]):
		data[name] = price

	return data


if __name__ == "__main__":
	pprint(parse_lukoil_data())
