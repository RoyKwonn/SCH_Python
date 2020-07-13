import urllib.request
import time

def get_price(country):    #함수 정의
    if country == "usa":
        page = urllib.request.urlopen("http://cs.sch.ac.kr/prices-loyalty.py")
        text = page.read().decode("utf8")
        where = text.find(">$")
        start_of_price = where + 2
        end_of_price = start_of_price + 4
    else :
        page = urllib.request.urlopen("http://cs.sch.ac.kr/prices1.py")
        text = page.read().decode("utf8")
        where = text.find("g>")
        start_of_price = where + 2
        end_of_price = start_of_price + 7
    return float(text[start_of_price:end_of_price])

price_now = input("긴급주문? (Y/N)")
if price_now == "Y":
    print("가격 --> ", get_price("kor"))
else :
    price = 5.5
    while price > 4.74:
        time.sleep(1)
        price = get_price("usa")
    print("지금 사세요 ", price)
        
