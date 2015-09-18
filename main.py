__author__ = 'jaehoonlee88'
import threading
import requests
import json
import datetime
import time

def printit():
    threading.Timer(60.0, printit).start()

    loc = ['gt', 'sandy', 'buckhead', 'marietta', 'decatur', 'alpharetta',  'peachtree', 'stone', 'piedmont']
    latitude = [33.775618, 33.9375, 33.8394, 33.9533, 33.7714, 34.0733, 33.3990, 33.8053, 33.783768]
    longtitude = [-84.396285,  -84.3686, -84.3799, -84.5406, -84.2978, -84.2811, -84.5706, -84.1714, -84.371889]

    for i in range(0, 8):
        print str(loc[i]) + ":" + str(latitude[i]) +',' + str(longtitude[i])
        #filename = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        #print (loc[i] + '/products/%s') % filename

        #products
        products_url = 'https://api.uber.com/v1/products'
        parameters = {
            'server_token': 'tBSlsqwP7AfaBIZfHDjd2nASkGDfuHmenwnBFznj',
            'latitude': latitude[i],
            'longitude': longtitude[i],
        }

        response = requests.get(products_url, params=parameters)
        data = response.json()
        filename = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        text_file = open((loc[i] + '/products/%s') % filename, "w")
        text_file.write(json.dumps(data, indent=4))
        text_file.close()

        #price estimates
        url = 'https://api.uber.com/v1/estimates/price'
        parameters = {
        'server_token': 'tBSlsqwP7AfaBIZfHDjd2nASkGDfuHmenwnBFznj',
        'start_latitude': latitude[i],
        'start_longitude': longtitude[i],
        'end_latitude': 33.783768,
        'end_longitude': -84.371889,
        }

        response = requests.get(url, params=parameters)
        data = response.json()
        filename = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        text_file = open((loc[i] + '/prices/%s') % filename, "w")
        text_file.write(json.dumps(data, indent=4))
        text_file.close()

        #time estimates
        url = 'https://api.uber.com/v1/estimates/time'
        parameters = {
            'server_token': 'tBSlsqwP7AfaBIZfHDjd2nASkGDfuHmenwnBFznj',
            'start_latitude': latitude[i],
            'start_longitude': longtitude[i],
        }

        response = requests.get(url, params=parameters)
        data = response.json()
        filename = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        text_file = open((loc[i] + '/times/%s') % filename, "w")
        text_file.write(json.dumps(data, indent=4))
        text_file.close()

        #promotion estimates
        url = 'https://api.uber.com/v1/promotions'
        parameters = {
        'server_token': 'tBSlsqwP7AfaBIZfHDjd2nASkGDfuHmenwnBFznj',
        'start_latitude': latitude[i],
        'start_longitude': longtitude[i],
        'end_latitude': 33.783768,
        'end_longitude': -84.371889,
        }

        response = requests.get(url, params=parameters)
        data = response.json()
        filename = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        text_file = open((loc[i] + '/promotion/%s') % filename, "w")
        text_file.write(json.dumps(data, indent=4))
        text_file.close()

    print "one loop : %s" % filename


    '''
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

    print "one loop : %s" % filename
    '''
printit()