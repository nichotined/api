import redis


class PyRedis(redis.Redis):
    def __init__(self, host='localhost', port=6379, db=0, password=None, socket_timeout=None,
                 socket_connect_timeout=None, socket_keepalive=None, socket_keepalive_options=None,
                 connection_pool=None, unix_socket_path=None, encoding='utf-8', encoding_errors='strict', charset=None,
                 errors=None, decode_responses=False, retry_on_timeout=False, ssl=False, ssl_keyfile=None,
                 ssl_certfile=None, ssl_cert_reqs='required', ssl_ca_certs=None, max_connections=None):
        super().__init__(host, port, db, password, socket_timeout, socket_connect_timeout, socket_keepalive,
                         socket_keepalive_options, connection_pool, unix_socket_path, encoding, encoding_errors,
                         charset, errors, decode_responses, retry_on_timeout, ssl, ssl_keyfile, ssl_certfile,
                         ssl_cert_reqs, ssl_ca_certs, max_connections)
