import os
import requests
import argparse

from urllib.parse import urlparse
from dotenv import load_dotenv
load_dotenv()


def shorten_link(token, url) :

    bitly_url = 'https://api-ssl.bitly.com/v4/shorten'
  
    headers = {'Authorization': 'Bearer {}'.format(token)}

    payload = {'long_url': url}
  
    response = requests.post(bitly_url, headers=headers, json=payload)
  
    response.raise_for_status()
    
    return response.json()['id']


def count_clicks(token, url):

    divided_url = urlparse(url)

    bitly_url = f'https://api-ssl.bitly.com/v4/bitlinks/{divided_url.netloc}{divided_url.path}/clicks/summary'
 
    headers = {'Authorization': 'Bearer {}'.format(token)}
  
    response = requests.get(bitly_url, headers=headers)
  
    response.raise_for_status()
  
    return response.json()['total_clicks']


def is_bitlink(url, api_key): 

    divided_url = urlparse(url)

    bitly_url = f'https://api-ssl.bitly.com/v4/bitlinks/{divided_url.netloc}{divided_url.path}'
      
    headers = {'Authorization': 'Bearer {}'.format(api_key)}
  
    response = requests.get(bitly_url, headers=headers)
  
    return response.ok

  
if __name__ == '__main__':
   
    parser = argparse.ArgumentParser(
        description='Программа сокращает ссылки и считает кол-во переходов по ней'
    )

    parser.add_argument('link', help='Ваша ссылка')

    args = parser.parse_args()

    api_key = os.environ['BITLY_API_KEY']
  
    response_ok = is_bitlink(args.link, api_key)

    try :

        if not response_ok :
      
            print('Битлинк: ', shorten_link(api_key, args.link))

        else: 

            print('По вашей ссылке прошли: {} раз(а)'.format(count_clicks(api_key, args.link)))
   
    except requests.exceptions.HTTPError as err:
    
        print("Во время выполнения произошла ошибка, статус ответа:", err)

    

  


