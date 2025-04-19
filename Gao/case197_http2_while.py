import httpx

cert_file = 'Gao/gao_apache/apache.gao.com.crt'
key_file = 'Gao/gao_apache/apache.gao.com.key'

def perform_request(url, headers):
    with httpx.Client(http2=True, verify=False, cert=(cert_file, key_file)) as client:
        response = client.get(url, headers=headers)
        print(f'Response from {url}: {response.text}')

def main():
    url = 'https://192.168.100.151:443'
    headers = {
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'upgrade-insecure-requests': '1',
        'cookie': 'M',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'accept-encoding': 'gzip, deflate, br',
        #'cookie': '',
        'cookie': 'rMhmPVeI9f5ISF9vjVnxKAIrcc727UCBe5AWl9FdmADCW1ZuXbuZEcoR6TnUQs0ZNh4JYlEEJW5zijxgU5eUnlCqmPMKPu27CDX0flsRElr6VzD3CB3bz14gDL3pwkiqg2afEU0SUHj4mbTkJvGnSKZBsrxft1rr9uUcMUxWxFdiAFEvznRpeIy49pm4iYr0jcQQgbGdscMRAKKaRC1Qfd1ayFRnfw7lVpNpdHndOHFJMEAQClFCJ30ee6dZpCC8kn7CVEiuJRlvUaDRE2Fe39jufvfgagmO4ShytJ7dDhmVeeZF17HeUcPi4PktrxE5vI0EkJX53RDf2bIUIXHfCh7aByeLXhcuRgEXShGd4Z0h5pBzFTzBocsM6vYeeOUltlqCKOlUtwrHQEGoYaIwzbzsC5PQhHtg8VC3uWxyuP9KQznM095OcDfDwd0kLMRvwi5hyxHBJ5WoxwnOGOTUouDRulH7tfMnQRv95UCpzxRoKMXuRKbTk9pIx6slt22r14ji1fmeArZmUyKKbl9tXBAjVMV4wGnWGBlEU81T7VY9LgE8qEQ8vXMqRyx1xo8c8oRRxog1E0ZlCcuVr8ODv8x5MdZuNsXTQC8SlJx1MLu4b9mYaYdoj1wetyhlgb9PAX5sszv2pCLU5GfTgFYeMzIRKfH9bCWsf10WL4FB9zgeIYrHBqzi8txjdbvjeZdoZknoBzhSQXwp5mMnLxPXnTEBrfi97xgTIgaaUd81kO7V7iwSvLSDfofRv8AQrh8fEap0hbZg1HZ1LzukShlF8ylWZyd0rwmv76yeUcz4Ynvn2HYNA0zk2ZFiZfoi123vob7SHhGWSwnKBBDT7drzzrggKXC5MTCDbNiad0UGXyqKdTPRMxkU5eTmJtpuGQIwChZvyd4KpotGyJWb8BVnJOy9FJfM3kWWMC9IeDlOEelusnVcwoWb0AHY0k7wX25g5Svuk4wEUltMDcHTVZfhyg4hBtPk4Rm8r5kx6eQO9oBf3tM6SwmSp7Tsj1iCMZY7',
        'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    while True:
        perform_request(url, headers)

if __name__ == '__main__':
    main()