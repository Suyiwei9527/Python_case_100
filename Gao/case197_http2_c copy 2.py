import http.client
import http2

def perform_request(host, path, headers):
    conn = http2.HTTP2Connection(host)
    conn.request('GET', path, headers=headers)
    response = conn.get_response()
    print(f'Response from {host}: {response.status}')

def main():
    host = 'example.com'
    path = '/'
    headers = {
        'User-Agent': 'My User Agent',
        'Custom-Header': 'Custom Value',
        'Connection': 'Upgrade, HTTP2-Settings',
        'Upgrade': 'h2c',
        'HTTP2-Settings': ''
    }

    while True:
        perform_request(host, path, headers)

if __name__ == '__main__':
    main()
