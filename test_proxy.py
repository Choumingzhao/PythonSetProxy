from myproxy import set_proxy, reset_proxy, set_wsl_proxy, get_ip

def is_wsl():
    import subprocess
    result = subprocess.run('/usr/bin/cat /proc/version', shell=True, capture_output=True).stdout
    if b'WSL' in result:
        return True
    else:
        return False

if __name__ == "__main__":
    if is_wsl():
        print("This is a WSL machine, using host as proxy")
        print(f"IP before setting: {get_ip()}")
        set_wsl_proxy()
        print(f"IP after setting: {get_ip()}")
        reset_proxy()
        print(f"IP after resetting: {get_ip()}")
    else:
        print(f"IP before setting: {get_ip()}")
        set_proxy()
        print(f"IP after setting: {get_ip()}")
        reset_proxy()
        print(f"IP after resetting: {get_ip()}")


