__author__ = 'jaehoonlee88'
import threading
import requests
import json
import datetime

def printit():
    threading.Timer(10.0, printit).start()

    #products
    products_url = 'https://api.uber.com/v1/products'
    parameters = {
    'server_token': 'tBSlsqwP7AfaBIZfHDjd2nASkGDfuHmenwnBFznj',
    'latitude': 33.775618,
    'longitude': -84.396285,
    }

    response = requests.get(products_url, params=parameters)
    data = response.json()
    filename = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    text_file = open('products/%s' % filename, "w")
    text_file.write(json.dumps(data, indent=4))
    text_file.close()

    #price estimates
    url = 'https://api.uber.com/v1/estimates/price'
    parameters = {
    'server_token': 'tBSlsqwP7AfaBIZfHDjd2nASkGDfuHmenwnBFznj',
    'start_latitude': 33.775618,
    'start_longitude': -84.396285,
    'end_latitude': 33.783768,
    'end_longitude': -84.371889,
    }

    response = requests.get(url, params=parameters)
    data = response.json()
    filename = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    text_file = open('prices/%s' % filename, "w")
    text_file.write(json.dumps(data, indent=4))
    text_file.close()

    #time estimates
    url = 'https://api.uber.com/v1/estimates/time'
    parameters = {
    'server_token': 'tBSlsqwP7AfaBIZfHDjd2nASkGDfuHmenwnBFznj',
    'start_latitude': 33.775618,
    'start_longitude': -84.396285,

    }

    response = requests.get(url, params=parameters)
    data = response.json()
    filename = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    text_file = open('times/%s' % filename, "w")
    text_file.write(json.dumps(data, indent=4))
    text_file.close()

    #promotion estimates
    url = 'https://api.uber.com/v1/promotions'
    parameters = {
    'server_token': 'tBSlsqwP7AfaBIZfHDjd2nASkGDfuHmenwnBFznj',
    'start_latitude': 33.775618,
    'start_longitude': -84.396285,
    'end_latitude': 33.783768,
    'end_longitude': -84.371889,
    }

    response = requests.get(url, params=parameters)
    data = response.json()
    filename = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    text_file = open('promotion/%s' % filename, "w")
    text_file.write(json.dumps(data, indent=4))
    text_file.close()


printit()