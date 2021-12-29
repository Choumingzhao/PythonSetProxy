# Seting the environment variable to the proxy server."""
import os

def get_current_ip():
    """
    Get if current geoIP corresponds to proxy setting.
    """
    import urllib.request as ur 
    import json
    return json.loads(ur.urlopen("https://api.ip.sb/geoip").read())

def set_proxy(proxy_server=None):
    """
    Set the proxy server for the current session.
    """
    if proxy_server:
        proxy_config = proxy_server
    else:
        # get IP of parent Windows machine
        nameserver = os.environ['nameserver']
        if nameserver:
            proxy_config = f"http://{nameserver}:17890"
        else:
            raise Exception("Cannot find IP for parent Windows machine.")

    os.environ['http_proxy'] = proxy_config
    os.environ['https_proxy'] = proxy_config

    # hot patch code to set proxy for urllib.request
    import urllib.request as ur
    proxy_handler = ur.ProxyHandler({'http': proxy_config,
                                    'https': proxy_config})
    opener = ur.build_opener(proxy_handler)
    ur.install_opener(opener)

    print(f'Proxy set to: {proxy_config}')

    return proxy_config

# default import myproxy: set proxy from environment variable "nameserver" for WSL
set_proxy()