import concurrent.futures
import httpx

def perform_request(url):
    headers = {
        'User-Agent': 'My User Agent',
        'Cookie': '',
        'Cookie': ''
    }
    with httpx.Client(http2=True, verify=False) as client:
        response = client.get(url, headers=headers)
        print(f"Response from {url}: {response.text}")

def main():
    urls = [
        'https://[192::101:151]:443/gao.php',
        'https://192.168.101.72/gao.html',
        'https://192.168.101.72/2233.html'
    ]
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(perform_request, urls)

if __name__ == '__main__':
    main()
