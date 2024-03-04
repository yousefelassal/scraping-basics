import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

load_dotenv()

# https://curlconverter.com/
cookies = {
    'ASP.NET_SessionId': os.getenv('SESSION_ID'),
    '.AspNet.Cookies': os.getenv('COOKIES'),
}

headers = {
    'authority': 'register.nu.edu.eg',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'content-type': 'application/json',
    'origin': 'https://register.nu.edu.eg',
    'referer': 'https://register.nu.edu.eg/PowerCampusSelfService/Registration/Courses',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Microsoft Edge";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0',
}

json_data = {
    'keyWords': 'csci',
    'yearTerm': '2024/SPRG',
}

response = requests.post(
    'https://register.nu.edu.eg/PowerCampusSelfService/Sections',
    cookies=cookies,
    headers=headers,
    json=json_data,
)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
data = '{"keyWords":"csci208","yearTerm":"2024/SPRG"}'
response = requests.post('https://register.nu.edu.eg/PowerCampusSelfService/Sections', cookies=cookies, headers=headers, data=data)

with open('response.json', 'w') as f:
    f.write(response.text)