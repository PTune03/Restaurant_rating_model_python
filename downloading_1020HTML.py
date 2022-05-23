# Скачивание 1020 страничек хтмл
import openpyxl
import requests

book = openpyxl.open("Tables/list_restaurants.xlsx", read_only= True)
sheet = book.active


url = "https://www.tripadvisor.ru/Restaurants-g298484-oa990-Moscow_Central_Russia.html#EATERY_LIST_CONTENTS"

headers = {
    "Accept": "*/*",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.174 YaBrowser/22.1.5.810 Yowser/2.5 Safari/537.36"
}
row = 600
for i in range(599, 1021):


    column = 1
    url = sheet[row][column].value
    req = requests.get(url, headers=headers)
    src = req.text
    title = sheet[row][0].value
    with open (f"Pages_html/{title}_page.html", "w", encoding="utf-8") as file:
        file.write(src)
    row +=1
    print("Страничка", title, "номер:", i, "Готова")

book.close()
