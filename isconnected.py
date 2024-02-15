import subprocess
import re

def is_hotspot_connected():
    try:
        result = subprocess.run(['networksetup', '-getinfo', 'Wi-Fi'], capture_output=True, text=True)
        output = result.stdout.lower()
        if 'ipv4 address:' in output and 'router:' in output:
            ipv4_address = re.search(r'ipv4 address:\s+(\S+)', output).group(1)
            router_address = re.search(r'router:\s+(\S+)', output).group(1)
            if ipv4_address.startswith("192.168.") and router_address.startswith("192.168."):
                return True
    except Exception as e:
        print("오류 발생:", e)
    return False

if __name__ == "__main__":
    if is_hotspot_connected():
        print("현재 핫스팟에 연결되어 있습니다.")
    else:
        print("현재 핫스팟에 연결되어 있지 않습니다.")
