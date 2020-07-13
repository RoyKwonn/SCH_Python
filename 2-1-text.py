import urllib.request

page = urllib.request.urlopen("http://cs.sch.ac.kr/prices.py")

text = page.read().decode("utf-8")


price = text[172:176]
print(price)

print(text)

