import requests


def get_quotes():
    response = requests.get('https://1c22eh3aj8.execute-api.us-east-1.amazonaws.com/challenge/quotes/')
    return response.json()


def get_quote(quote_number):
    response = requests.get('https://1c22eh3aj8.execute-api.us-east-1.amazonaws.com/challenge/quotes/{}'.format(quote_number))
    return response.json()
