import requests, re

channels = {
    "VTV1 HD": "vtv1-hd",
    "VTV2 HD": "vtv2-hd",
    "VTV3 HD": "vtv3-hd",
    "VTV4 HD": "vtv4-hd",
    "VTV5 HD": "vtv5-hd",
    "VTV7 HD": "vtv7-hd",
    "VTV8 HD": "vtv8-hd",
    "VTV9 HD": "vtv9-hd",
}

m3u_content = "#EXTM3U\n"
for name, slug in channels.items():
    try:
        r = requests.get(f"https://vtvgo.vn/live/{slug}", timeout=10)
        m3u8_url = re.search(r'https.*?\.m3u8', r.text).group()
        m3u_content += f'#EXTINF:-1 group-title="VTV",{name}\n{m3u8_url}\n'
    except:
        pass

with open("playlist.m3u", "w", encoding="utf-8") as f:
    f.write(m3u_content)
