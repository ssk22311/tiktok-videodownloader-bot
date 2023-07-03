from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen


cookies = {
    '_gid': 'GA1.2.365766600.1687942808',
    '__cflb': '0H28v8EEysMCvTTqtu4Ydr4bADFLp2DZaQsmCMfKzMK',
    '__gads': 'ID=2ad6c59135b539ad-2233df97adb400c2:T=1687942808:RT=1687943172:S=ALNI_MbwMw9yYXfzy7D-Qrfq_gd_mOZtDA',
    '__gpi': 'UID=00000c774751c7ea:T=1687942808:RT=1687943172:S=ALNI_MY-nKX-QkUOHMlUgBpVSV5brstSAQ',
    '_gat_UA-3524196-6': '1',
    '_ga': 'GA1.2.942987829.1687942808',
    '_ga_ZSF3D6YSLC': 'GS1.1.1687942808.1.1.1687943325.0.0.0',
}

headers = {
    'authority': 'ssstik.io',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,fr;q=0.6',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': '_gid=GA1.2.365766600.1687942808; __cflb=0H28v8EEysMCvTTqtu4Ydr4bADFLp2DZaQsmCMfKzMK; __gads=ID=2ad6c59135b539ad-2233df97adb400c2:T=1687942808:RT=1687943172:S=ALNI_MbwMw9yYXfzy7D-Qrfq_gd_mOZtDA; __gpi=UID=00000c774751c7ea:T=1687942808:RT=1687943172:S=ALNI_MY-nKX-QkUOHMlUgBpVSV5brstSAQ; _gat_UA-3524196-6=1; _ga=GA1.2.942987829.1687942808; _ga_ZSF3D6YSLC=GS1.1.1687942808.1.1.1687943325.0.0.0',
    'hx-current-url': 'https://ssstik.io/en#google_vignette',
    'hx-request': 'true',
    'hx-target': 'target',
    'hx-trigger': '_gcaptcha_pt',
    'origin': 'https://ssstik.io',
    'referer': 'https://ssstik.io/en',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
}

params = {
    'url': 'dl',
}

def downloadVideo(link, id):
    print(f"Downloading video {id} from: {link}")

    data = {
    'id': link,
    'locale': 'en',
    'tt': 'VmRxMkRh',
    }

    response = requests.post('https://ssstik.io/abc', params=params, cookies=cookies, headers=headers, data=data)
    downloadSoup = BeautifulSoup(response.text, "html.parser")
    downloadLink = downloadSoup.a["href"]
    mp4File = urlopen(downloadLink)
    with open(f"{id}.mp4", "wb") as output:
        while True:
           data = mp4File.read(4096)
           if data:
              output.write(data)
           else:
              break
