import subprocess

def is_wifi_connected():
    try:
        result = subprocess.run(['networksetup', '-getairportnetwork', 'en0'], capture_output=True, text=True)
        output = result.stdout.lower()
        if 'current wi-fi network' in output:
            return True
    except Exception as e:
        print("오류 발생:", e)
    return False

def is_hotspot_connected():
    try:
        result = subprocess.run(['networksetup', '-getairportnetwork', 'en0'], capture_output=True, text=True)
        output = result.stdout.lower()
        if 'current wi-fi network' not in output:
            return True
    except Exception as e:
        print("오류 발생:", e)
    return False

if __name__ == "__main__":
    if is_wifi_connected():
        print("현재 Wi-Fi에 연결되어 있습니다.")
    elif is_hotspot_connected():
        print("현재 핫스팟에 연결되어 있습니다.")
    else:
        print("현재 Wi-Fi 또는 핫스팟에 연결되어 있지 않습니다.")
