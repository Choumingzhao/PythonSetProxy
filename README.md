# Python set proxy

Hot patch proxy setting for Python script and Jupyter Notebook

usage:

## Set proxy from WSL's parent Windows machine

```python
import myproxy
```

## Set proxy manually  

```python
from myproxy import set_proxy
set_proxy('http://localhost:8080')
```

## Check current ip

```python
from myproxy import get_current_ip
get_current_ip()
```
