# Seting the environment variable to the proxy server."""
import os

def get_current_ip():
    """
    Get if current geoIP corresponds to proxy setting.
    """
    import urllib.request as ur 
    import json
    return json.loads(ur.urlopen("https://api.ip.sb/geoip").read())

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