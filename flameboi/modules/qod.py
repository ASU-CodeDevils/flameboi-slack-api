import requests


def getQOD() -> list:

    output = []

    url = 'https://quotes.rest/qod'
    api_token = "YOUR API KEY HERE"
    headers = {'content-type': 'application/json',
        'X-TheySaidSo-Api-Secret': format(api_token)}

    response = requests.get(url, headers=headers)
    #print(response)
    output.append(response.json()['contents']['quotes'][0]['quote'])
    output.append(response.json()['contents']['quotes'][0]['author'])

    return output