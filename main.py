from cfg import Config
import requests
import json


def main():
    cfg = Config().cfg
    base_url = 'https://api.nal.usda.gov/fdc'
    api_ver = 'v1'

    raw_response = requests.get(url=f"{base_url}/{api_ver}/foods/list?api_key={cfg['api_key']}")
    foods = json.loads(raw_response.text)


if __name__ == '__main__':
    main()
