import requests
import json
from json_hw import JsonHandler
from requests.auth import HTTPBasicAuth


def get_id(cur, abb):
    for id, elem, _ in cur:
        if elem == abb:
            return id


if __name__ == "__main__":
    link = 'https://api.nbrb.by/exrates/'

    # Task 1
    response = requests.get(
        link + f'currencies/'
    )
    json_response = JsonHandler(json.dumps(response.json()))
    currencies = list(json_response.print_key(('Cur_ID','Cur_Abbreviation','Cur_Name_Eng')))
    print(currencies)

    # Task 2
    for abbr in ['USD', 'EUR']:
        response = requests.get(
            link + f'rates/{abbr}',
            params={"parammode": 2, "periodicity": 1}
        ).json()
        print(f"{response['Cur_Abbreviation']}: {response['Cur_OfficialRate']}")

    # Task 3
    target = {'USD', 'COP', 'MNT', 'ESP'}
    response = requests.get(
        link + f'currencies'
    ).json()
    for elem in response:
        if elem['Cur_Abbreviation'] in target:
            print(f"{elem['Cur_Abbreviation']}: {elem['Cur_Name']}, {elem['Cur_Name_Bel']}, {elem['Cur_Name_Bel']}")

    # Task 4
    for abb in ['USD']:
        response = requests.get(
            link + f'rates/{abbr}',
            params={"parammode": 2, "periodicity": 1, "ondate":'2019-02-06'}
        ).json()

        def format_to(x):
            return "{:.4f}".format(x)

        print(f"{abb} for {response['Date']}: {response['Cur_OfficialRate']}, for 100 BYN you can get {format_to(100 / response['Cur_OfficialRate'])} USD")
