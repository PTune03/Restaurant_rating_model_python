# Считывание страничек, со списком ресторанов
import requests
import openpyxl
from bs4 import BeautifulSoup
url = "https://www.tripadvisor.ru/Restaurants-g298484-oa990-Moscow_Central_Russia.html#EATERY_LIST_CONTENTS"

headers = {
    "Accept": "*/*",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.174 YaBrowser/22.1.5.810 Yowser/2.5 Safari/537.36"
}

req = requests.get(url, headers=headers)
src = req.text
count = 34
with open (f"list_restaurants_pages/{count}_page.html", "w", encoding="utf-8") as file:
    file.write(src)

# Запись всех ресторанов в EXCEL

book = openpyxl.Workbook()
sheet = book.active
sheet['A1'] = 'Название ресторана'
sheet['B1'] = 'Ссылка'
url = "https://www.tripadvisor.ru/Restaurants-g298484-oa990-Moscow_Central_Russia.html#EATERY_LIST_CONTENTS"

headers = {
    "Accept": "*/*",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.174 YaBrowser/22.1.5.810 Yowser/2.5 Safari/537.36"
}
count = 34
row = 2
for count in range(1,35):

    with open (f"list_restaurants_pages/{count}_page.html",encoding="utf-8") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")
    restaurants_hrefs = soup.find_all(class_="bHGqj Cj b")


    for item in restaurants_hrefs:
        item_text = item.text
        item_href = "https://www.tripadvisor.ru" + item.get("href")

        sheet[row][0].value = item_text
        sheet[row][1].value = item_href
        row += 1



book.save("Tables/list_restaurants.xlsx")
book.close()
