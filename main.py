
import pywifi
from pywifi import const

wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0]

iface.scan() 
results = iface.scan_results()

for result in results:
    profile = pywifi.Profile()
    profile.ssid = result.ssid
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)

    profile.cipher = const.CIPHER_TYPE_CCMP
    profile.key = None

    iface.remove_all_network_profiles()
    tmp_profile = iface.add_network_profile(profile)
    iface.connect(tmp_profile)
    if iface.status() == const.IFACE_CONNECTED:
        print(f"Password for {result.ssid}: {profile.key}")
        break 
