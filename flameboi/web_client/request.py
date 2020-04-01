import requests


def get(url: str, params: dict = None) -> dict:
    """
    Makes a GET request against a specified URL.
    :param url: The URL endpoint.
    :param params: Additional request parameters.
    :return: The response as a dict.
    """
    try:
        response = requests.get(url=url, params=params)
        return response.json()
    except Exception as e:
        raise Exception(f'Error making GET request to {url}: {str(e)}')


def post(url: str, data: dict = None) -> dict:
    """
    Makes a POST request against a specified URL.
    :param url: The URL endpoint.
    :param data: Request body to send with request.
    :return: The response as a dict.
    """
    try:
        response = requests.post(url=url, data=data)
        return response.json()
    except Exception as e:
        raise Exception(f'Error making POST request to {url}: {str(e)}')
