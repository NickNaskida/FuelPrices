from pprint import pprint

from gulf_parser import parse_gulf_data
from rompetrol_parser import parse_rompetrol_data
from wissol_parser import parse_wissol_data
from lukoil_parser import parse_lukoil_data
from socar_parser import parse_socar_data


if __name__ == "__main__":
	pprint(parse_gulf_data())
	pprint(parse_rompetrol_data())
	pprint(parse_wissol_data())
	pprint(parse_lukoil_data())
	pprint(parse_socar_data())
