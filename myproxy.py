# Seting the environment variable to the proxy server."""
import requests as rq
import os

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
    """Set the proxy server by environment variable for higher version of python3"""
    proxy_server = f"{host}:{port}"
    os.environ['HTTP_PROXY'] = proxy_server
    os.environ['HTTPS_PROXY'] = proxy_server
    os.environ['ALL_PROXY'] = proxy_server
    if verbose:
        print(f"Setting proxy to {proxy_server}")

def reset_proxy(verbose=True):
    ## This only affect os.system, popen, for and execv
    #os.unsetenv('HTTP_PROXY')
    #os.unsetenv('HTTPS_PROXY')
    #os.unsetenv('ALL_PROXY')
    # This actually delete the environment variables
    os.environ.pop('HTTP_PROXY')
    os.environ.pop('HTTPS_PROXY')
    os.environ.pop('ALL_PROXY')
    if verbose:
        print(f"Unsetting all proxies settings")

def set_wsl_proxy():
    host = os.environ.get('nameserver', 'localhost')
    set_proxy(host, 17890)

#def set_proxy(proxy_server=None):
#    """
#    Set the proxy server for the current session by settting urllib.request ProxyHandler
#    """
#    if proxy_server:
#        proxy_config = proxy_server
#    else:
#        # get IP of parent Windows machine for WSL machine
#        nameserver = os.environ.get('nameserver', 'localhost')
#        proxy_config = f"http://{nameserver}:17890"
#    os.environ['http_proxy'] = proxy_config
#    os.environ['https_proxy'] = proxy_config
#
#    # hot patch code to set proxy for urllib.request
#    import urllib.request as ur
#    proxy_handler = ur.ProxyHandler({'http': proxy_config,
#                                    'https': proxy_config})
#    opener = ur.build_opener(proxy_handler)
#    ur.install_opener(opener)
#
#    print(f'Proxy set to: {proxy_config}')
#
#    return proxy_config
#
# default import myproxy: set proxy from environment variable "nameserver" for WSL
# set_proxy()
