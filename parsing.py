# Парсинг 1000 хтмл страничек, добыча инфы, запись ее в эксель табличку


from bs4 import BeautifulSoup
import openpyxl

book = openpyxl.open("Tables/list_restaurants.xlsx", read_only= True)
sheet = book.active
array = []
for i in range(1,1021):
    array.append(sheet[i+1][0].value)

book.close()

book = openpyxl.Workbook()
sheet = book.active
sheet['A1'] = "Название"
sheet['B1'] = "Количество отзывов"
sheet['C1'] = "Ценовой диапазон"
sheet['D1'] = "Тип кухни"
sheet['E1'] = "Специализированное меню"
sheet['F1'] = "Адрес"
sheet['G1'] = "Телефон"
sheet['H1'] = "Почта"
sheet['I1'] = "Рейтинг еды"
sheet['J1'] = "Рейтинг сервиса"
sheet['K1'] = "Цена/качество"
url = "https://www.tripadvisor.ru/Restaurants-g298484-oa990-Moscow_Central_Russia.html#EATERY_LIST_CONTENTS"

headers = {
    "Accept": "*/*",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.174 YaBrowser/22.1.5.810 Yowser/2.5 Safari/537.36"
}
counter = 0
row = 2
for i in range(1, 1021):

    with open(f"Pages_html/{array[i - 1]}_page.html", encoding="utf-8") as file:
        src = file.read()
    soup = BeautifulSoup(src, "lxml")

    name = soup.find(class_="fHibz")
    if name is None:
        print("pizdec")
    else:
        name = name.text
    num_reviews = soup.find(class_="eBTWs")
    if num_reviews is None:
        continue
    else:
        num_reviews = num_reviews.text

    rep = ['\xa0', '\xa0PM', '\xa0PM']

    details = soup.find_all(class_="cfvAV")
    price_range = details[0].text
    for item in rep:
        if item in price_range:
            price_range = price_range.replace(item, "")
    # print(price_range)
    if len(details) < 2:
        print("strange things happens")
    else:
        type_kitchen = details[1].text
    # print(type_kitchen)
    if len(details) < 3:
        print("strange things happens 2")
    else:
        specialised_menu = details[2].text
    # print(specialised_menu)
    address = soup.find(class_="brMTW").text
    # print(address)
    details = soup.find_all(class_="iPqaD _F G- ddFHE eKwUx")
    if len(details) < 2:
        print("no telephone")
    else:
        telephone = details[1].text
    # print(telephone)
    details = soup.find_all(class_="bKBJS Me enBrh")
    mail = details[1].find("a")
    if mail is None:
        print("Почты нема")
    else:
        mail = mail.get("href")
        # print(mail)
    ratings = soup.find_all(class_="cGQpb")
    if not ratings:
        print("asshole")
    else:
        if len(ratings) < 1:
            print("rating is less than 1")
        else:
            feeding_rating = ratings[0].find(class_="cwxUN")
        if len(ratings) < 2:
            print("rating is less than 2 ")
        else:
            service_rating = ratings[1].find(class_="cwxUN")
        if len(ratings) < 3:
            print("rating is less than 3")
        else:
            price_quality = ratings[2].find(class_="cwxUN")
        feeding_rating = str(feeding_rating)
        rep = ['</span>', '<span class=', '><span class=', '"cwxUN"', '>','"']
        for item in rep:
            if item in feeding_rating:
                feeding_rating = feeding_rating.replace(item,"")
        feeding_rating = int(feeding_rating[-2:])/10
        # print(feeding_rating)

        service_rating = str(service_rating)
        for item in rep:
            if item in service_rating:
                service_rating = service_rating.replace(item,"")
        service_rating = int(service_rating[-2:])/10
        # print(service_rating)

        price_quality = str(price_quality)
        for item in rep:
            if item in price_quality:
                price_quality = price_quality.replace(item,"")
        if price_quality:
            if counter == 466 or counter == 939 or counter == 977:
                price_quality = 4
                if counter == 939:
                    price_quality = 3.5
                if counter == 977:
                    price_quality = 4.5
            else:
                price_quality = int(price_quality[-2:])/10
        else:
            print("no price quality")
    # print(price_quality)

    sheet[row][0].value = name
    sheet[row][1].value = num_reviews
    sheet[row][2].value = price_range
    sheet[row][3].value = type_kitchen
    sheet[row][4].value = specialised_menu
    sheet[row][5].value = address
    sheet[row][6].value = telephone
    sheet[row][7].value = mail
    sheet[row][8].value = feeding_rating
    sheet[row][9].value = service_rating
    sheet[row][10].value = price_quality
    row += 1

    counter +=1
    print("Ресторан номер:", counter, "готово")

book.save("Tables/dataset.xlsx")
book.close()