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

m3u_lines = ["#EXTM3U\n"]
for name, slug in channels.items():
    try:
        resp = requests.get(f"https://vtvgo.vn/live/{slug}", timeout=15)
        match = re.search(r"https?://[^\"]+\.m3u8", resp.text)
        if match:
            m3u_lines.append(f"#EXTINF:-1,{name}\n{match.group()}\n")
    except Exception as e:
        print(f"Error fetching {name}: {e}")

with open("playlist.m3u", "w", encoding="utf-8") as f:
    f.writelines(m3u_lines)
