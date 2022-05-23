import requests
from bs4 import BeautifulSoup
import json

headers = {
    "Accept": "*/*",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.174 YaBrowser/22.1.5.810 Yowser/2.5 Safari/537.36"
}

with open("restaurants_dict.json") as file:
    page = json.load(file)

print(page)
