# Seting the environment variable to the proxy server."""
import os
import requests as rq
from six.moves import urllib

def get_ip():
    """
    Get if current IP corresponds to proxy setting.
    """
    headers = {'user-agent': 'Mozzila Firefox'}
    return rq.get('https://api.ip.sb/ip', headers=headers).text

def get_geoip():
    """
    Get if current geoIP corresponds to proxy setting.
    """
    headers = {'user-agent': 'Mozzila Firefox'}
    return rq.get('https://api.ip.sb/geoip', headers=headers).json()

def set_proxy(host='localhost', port='17890', verbose=True):
    """
    Sets the proxy server using a ProxyHandler for urllib applications.

    Args:
        host (str, optional): The proxy server hostname. Defaults to 'localhost'.
        port (str, optional): The proxy server port. Defaults to '17890'.
        verbose (bool, optional): Whether to print verbose messages. Defaults to True.
    """
    proxy_server = f"http://{host}:{port}"
    proxy_handler = urllib.request.ProxyHandler({'http': proxy_server,
                                                 'https': proxy_server})

    # Create a new opener using the ProxyHandler
    opener = urllib.request.build_opener(proxy_handler)

    # Install the opener globally for urllib requests
    urllib.request.install_opener(opener)


    # Additional lines to set proxy for requests
    os.environ['HTTP_PROXY'] = proxy_server
    os.environ['HTTPS_PROXY'] = proxy_server
    os.environ['ALL_PROXY'] = proxy_server
    if verbose:
        print(f"Setting proxy to {proxy_server}")

def reset_proxy(verbose=True):
    """
    Resets the proxy settings for urllib applications.

    Args:
        verbose (bool, optional): Whether to print verbose messages. Defaults to True.
    """
    # Reset the global opener
    urllib.request.install_opener(None)

    ## This only affect os.system, popen, for and execv
    #os.unsetenv('HTTP_PROXY')
    #os.unsetenv('HTTPS_PROXY')
    #os.unsetenv('ALL_PROXY')
    # Additional lines to reset proxy for requests
    os.environ.pop('HTTP_PROXY', None)
    os.environ.pop('HTTPS_PROXY', None)
    os.environ.pop('ALL_PROXY', None)
    if verbose:
        print("Unsetting proxy settings")
def set_wsl_proxy():
    host = os.environ.get('nameserver', 'localhost')
    set_proxy(host, 17890)
