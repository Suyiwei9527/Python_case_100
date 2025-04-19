import httpcore
import httpx

headers1 = {'Connection': 'Keep-Alive',
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'sec-fetch-site': 'none',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'cookie': 'rMhmPVeI9f5ISF9vjVnxKAIrcc727UCBe5AWl9FdmADCW1ZuXbuZEcoR6TnUQs0ZNh4JYlEEJW5zijxgU5eUnlCqmPMKPu27CDX0flsRElr6VzD3CB3bz14gDL3pwkiqg2afEU0SUHj4mbTkJvGnSKZBsrxft1rr9uUcMUxWxFdiAFEvznRpeIy49pm4iYr0jcQQgbGdscMRAKKaRC1Qfd1ayFRnfw7lVpNpdHndOHFJMEAQClFCJ30ee6dZpCC8kn7CVEiuJRlvUaDRE2Fe39jufvfgagmO4ShytJ7dDhmVeeZF17HeUcPi4PktrxE5vI0EkJX53RDf2bIUIXHfCh7aByeLXhcuRgEXShGd4Z0h5pBzFTzBocsM6vYeeOUltlqCKOlUtwrHQEGoYaIwzbzsC5PQhHtg8VC3uWxyuP9KQznM095OcDfDwd0kLMRvwi5hyxHBJ5WoxwnOGOTUouDRulH7tfMnQRv95UCpzxRoKMXuRKbTk9pIx6slt22r14ji1fmeArZmUyKKbl9tXBAjVMV4wGnWGBlEU81T7VY9LgE8qEQ8vXMqRyx1xo8c8oRRxog1E0ZlCcuVr8ODv8x5MdZuNsXTQC8SlJx1MLu4b9mYaYdoj1wetyhlgb9PAX5sszv2pCLU5GfTgFYeMzIRKfH9bCWsf10WL4FB9zgeIYrHBqzi8txjdbvjeZdoZknoBzhSQXwp5mMnLxPXnTEBrfi97xgTIgaaUd81kO7V7iwSvLSDfofRv8AQrh8fEap0hbZg1HZ1LzukShlF8ylWZyd0rwmv76yeUcz4Ynvn2HYNA0zk2ZFiZfoi123vob7SHhGWSwnKBBDT7drzzrggKXC5MTCDbNiad0UGXyqKdTPRMxkU5eTmJtpuGQIwChZvyd4KpotGyJWb8BVnJOy9FJfM3kWWMC9IeDlOEelusnVcwoWb0AHY0k7wX25g5Svuk4wEUltMDcHTVZfhyg4hBtPk4Rm8r5kx6eQO9oBf3tM6SwmSp7Tsj1iCMZY7',
            'cookie': '$%$^$%^$^$^$',
            'cookie': '!@#$%^&*(),.,,.,',
            'cookie': '$%$^$%^$^$^$',
            'cookie': '$%$^$%^$^$^$',
            'cookie': '$%$^$%^$^$^$',
            'cookie': '$%$^$%^$^$^$',
            'cookie': '$%$^$%^$^$^$',
            'cookie': '$%$^$%^$^$^$',
            'cookie': '$%$^$%^$^$^$',
            'cookie': '$%$^$%^$^$^$',
            'cookie': '$%$^$%^$^$^$',
            'cookie': '$%$^$%^$^$^$',
            'cookie': '$%$^$%^$^$^$',
            'cookie': '$%$^$%^$^$^$',
            'cookie': '$%$^$%^$^$^$',
            'cookie': '''      
            
            
            
            
            
            ''',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
            }

url0 = 'https://192.168.101.72:443/gao.php'
url1  = 'https://test-ssc.mohrss.gov.cn/api/token?_api_timestamp=1683365525551&security=67IChDqqX7TaPyhLc%2B5Ieen5ways9iBrsCo9D8VbYDdDWg8ZIy47whCNKhrwQQO%2FqkeZpsKLLMl%2BnJ5baSE1hDU7wQGOo3%2F8ysiTX8nJ44uUAkhdWjYBNHJX17PkPo4w4FEw%2FbeUSPp9XO3lRZLpwk1Mh1oybL1gV%2Fl9yfc5uHXjZTbIrNnOzWZ2%2F6CpyumKsn6PVrNk1x4NWx3nMswj%2BIqbJAnIQoqfQEmER2vaUOxkVq6C1KJtR8Hqv9T42PBjX5hn6CqgMyRprFAOd34qZCSuKBalaRS1ZP8YJyfCHEqyKvQIOXfRIq3hLcdrotOmFinuq2LNhCbE57UhNCrh1whJKWDM6kkaMGZWtAUDrjm5dKIm0yjoYuWuCdNZ2tk2BnZfDMz6d%2BdW38O0G4gTzArN2Z3uQS29XKDdyhHCXrgfMl3TyPeKxbTitLSxY4lgk3YlPRxP7SMAOb7fAgN5R2dvg4Bql9OdljY4tR%2Bn%2FsQtZ4O0hOKPKK4od28kaLYbNrjunpcqd3Gh4okOm7Up%2FySTXCWEzEM9%2BF5P895v1tx6DzFh0Wz6AOeWbgi6ZzJYljlhBn%2FfxL%2FBwbjLA5X%2FfwriU%2BXi9%2B3m2alFPwgBo6Vv%2FpIegQVMMuP1h722vVpAnwqqgq0yUa5xSEqVQ%2F5Plzg7V442rBOke7s73PauHT51ZvdEU5w86ywu896ufL7csbNWe2NogIbVduBlSXv8ZJA1Zze2jfpcJbu3%2FRthHIzSm%2ByfFCJ17Ltma2ID0WIwjowrpObOayapxL3a15VjazaPST%2B9vQp2hsnflAVxblfwyXRyWrFVtEY4Hwa7MrLQVA4W5XAeTQaHnOATxXg8xhPCEc2dgD50qO7gxaPpdNN0p%2FBwboP1y54Hgd2AYsgTndsO0hIISPXwVNPkwlSS0wp1XK9Q2BlbZvLdg4vNWGY%3D&_api_name=get_token&api_access_key=3b8c9c74f41f43c1a6f43be9b2e7c8b8&_api_signature=OucQREN6DlyNYhemsWyuHrBksCc%3D&return_url=http:%2F%2F39.105.151.133%2Fportal%2Fhealth%2F&_api_version=1.0.0&_api_access_key=3b8c9c74f41f43c1a6f43be9b2e7c8b8'
url3 = 'https://test-ssc.mohrss.gov.cn/iframe-h5/index.html'
url5 = 'https://test-ssc.mohrss.gov.cn/favicon.ico'
url7  = 'https://test-ssc.mohrss.gov.cn/api/token?_api_timestamp=1683365525551&security=67IChDqqX7TaPyhLc%2B5Ieen5ways9iBrsCo9D8VbYDdDWg8ZIy47whCNKhrwQQO%2FqkeZpsKLLMl%2BnJ5baSE1hDU7wQGOo3%2F8ysiTX8nJ44uUAkhdWjYBNHJX17PkPo4w4FEw%2FbeUSPp9XO3lRZLpwk1Mh1oybL1gV%2Fl9yfc5uHXjZTbIrNnOzWZ2%2F6CpyumKsn6PVrNk1x4NWx3nMswj%2BIqbJAnIQoqfQEmER2vaUOxkVq6C1KJtR8Hqv9T42PBjX5hn6CqgMyRprFAOd34qZCSuKBalaRS1ZP8YJyfCHEqyKvQIOXfRIq3hLcdrotOmFinuq2LNhCbE57UhNCrh1whJKWDM6kkaMGZWtAUDrjm5dKIm0yjoYuWuCdNZ2tk2BnZfDMz6d%2BdW38O0G4gTzArN2Z3uQS29XKDdyhHCXrgfMl3TyPeKxbTitLSxY4lgk3YlPRxP7SMAOb7fAgN5R2dvg4Bql9OdljY4tR%2Bn%2FsQtZ4O0hOKPKK4od28kaLYbNrjunpcqd3Gh4okOm7Up%2FySTXCWEzEM9%2BF5P895v1tx6DzFh0Wz6AOeWbgi6ZzJYljlhBn%2FfxL%2FBwbjLA5X%2FfwriU%2BXi9%2B3m2alFPwgBo6Vv%2FpIegQVMMuP1h722vVpAnwqqgq0yUa5xSEqVQ%2F5Plzg7V442rBOke7s73PauHT51ZvdEU5w86ywu896ufL7csbNWe2NogIbVduBlSXv8ZJA1Zze2jfpcJbu3%2FRthHIzSm%2ByfFCJ17Ltma2ID0WIwjowrpObOayapxL3a15VjazaPST%2B9vQp2hsnflAVxblfwyXRyWrFVtEY4Hwa7MrLQVA4W5XAeTQaHnOATxXg8xhPCEc2dgD50qO7gxaPpdNN0p%2FBwboP1y54Hgd2AYsgTndsO0hIISPXwVNPkwlSS0wp1XK9Q2BlbZvLdg4vNWGY%3D&_api_name=get_token&api_access_key=3b8c9c74f41f43c1a6f43be9b2e7c8b8&_api_signature=OucQREN6DlyNYhemsWyuHrBksCc%3D&return_url=http:%2F%2F39.105.151.133%2Fportal%2Fhealth%2F&_api_version=1.0.0&_api_access_key=3b8c9c74f41f43c1a6f43be9b2e7c8b8'
url9 = 'https://test-ssc.mohrss.gov.cn/portal/forward/sign?service=/sign/v2/channel/query/sign/info'
url11 = 'https://test-ssc.mohrss.gov.cn/portal/forward/service?service=/service/v2/query/queryUserInfo'
url13 = 'https://test-ssc.mohrss.gov.cn/portal/forward/sign?service=/sign/v2/sign/validSign'
url15 = 'https://test-ssc.mohrss.gov.cn/logCollect/log/collect/print/local'
url17 = 'https://test-ssc.mohrss.gov.cn/portal/forward/service?service=/service/v2/ocp/service/sector/query'
url19 = 'https://test-ssc.mohrss.gov.cn/portal/forward/service?service=/service/v3/page/skin'
url21 = 'https://test-ssc.mohrss.gov.cn/portal/forward/publish?service=/message/center/recordCountV1'
url23 = 'https://test-ssc.mohrss.gov.cn/portal/forward/service?service=/service/v2/page/ecard'
url25 = 'https://test-ssc.mohrss.gov.cn/portal/forward/service?service=/service/v3/page/recommend/service'
url27 = 'https://test-ssc.mohrss.gov.cn/portal/forward/publish?service=/ecard/v1/cms/bannerList'
url29 = 'https://test-ssc.mohrss.gov.cn/portal/forward/service?service=/service/v3/page/tips/query'
url31 = 'https://test-ssc.mohrss.gov.cn/portal/forward/service?service=/service/v2/init/protocols/check'
url33 = 'https://test-ssc.mohrss.gov.cn/portal/forward/publish?service=/cms/popup/findPopByRegion'
url35 = 'https://test-ssc.mohrss.gov.cn/portal/forward/service?service=/service/v3/page/service/is/exist'
url37 = 'https://test-ssc.mohrss.gov.cn//api/token?_api_timestamp=1683365525551&security=67IChDqqX7TaPyhLc%2B5Ieen5ways9iBrsCo9D8VbYDdDWg8ZIy47whCNKhrwQQO%2FqkeZpsKLLMl%2BnJ5baSE1hDU7wQGOo3%2F8ysiTX8nJ44uUAkhdWjYBNHJX17PkPo4w4FEw%2FbeUSPp9XO3lRZLpwk1Mh1oybL1gV%2Fl9yfc5uHXjZTbIrNnOzWZ2%2F6CpyumKsn6PVrNk1x4NWx3nMswj%2BIqbJAnIQoqfQEmER2vaUOxkVq6C1KJtR8Hqv9T42PBjX5hn6CqgMyRprFAOd34qZCSuKBalaRS1ZP8YJyfCHEqyKvQIOXfRIq3hLcdrotOmFinuq2LNhCbE57UhNCrh1whJKWDM6kkaMGZWtAUDrjm5dKIm0yjoYuWuCdNZ2tk2BnZfDMz6d%2BdW38O0G4gTzArN2Z3uQS29XKDdyhHCXrgfMl3TyPeKxbTitLSxY4lgk3YlPRxP7SMAOb7fAgN5R2dvg4Bql9OdljY4tR%2Bn%2FsQtZ4O0hOKPKK4od28kaLYbNrjunpcqd3Gh4okOm7Up%2FySTXCWEzEM9%2BF5P895v1tx6DzFh0Wz6AOeWbgi6ZzJYljlhBn%2FfxL%2FBwbjLA5X%2FfwriU%2BXi9%2B3m2alFPwgBo6Vv%2FpIegQVMMuP1h722vVpAnwqqgq0yUa5xSEqVQ%2F5Plzg7V442rBOke7s73PauHT51ZvdEU5w86ywu896ufL7csbNWe2NogIbVduBlSXv8ZJA1Zze2jfpcJbu3%2FRthHIzSm%2ByfFCJ17Ltma2ID0WIwjowrpObOayapxL3a15VjazaPST%2B9vQp2hsnflAVxblfwyXRyWrFVtEY4Hwa7MrLQVA4W5XAeTQaHnOATxXg8xhPCEc2dgD50qO7gxaPpdNN0p%2FBwboP1y54Hgd2AYsgTndsO0hIISPXwVNPkwlSS0wp1XK9Q2BlbZvLdg4vNWGY%3D&_api_name=get_token&api_access_key=3b8c9c74f41f43c1a6f43be9b2e7c8b8&_api_signature=OucQREN6DlyNYhemsWyuHrBksCc%3D&return_url=http:%2F%2F39.105.151.133%2Fportal%2Fhealth%2F&_api_version=1.0.0&_api_access_key=3b8c9c74f41f43c1a6f43be9b2e7c8b8'

cert_file = 'Gao/gao_apache/apache.gaov_755.com.crt'
key_file = 'Gao/gao_apache/apache.gaov_755.com.key'

with httpx.Client(headers=headers1, verify=False, http2=True, cert=(cert_file, key_file)) as client:

    r1 = client.get(url0 , headers=headers1)
    print(r1)