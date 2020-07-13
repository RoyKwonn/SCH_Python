class Address():
    name = ""
    line1 = ""
    line2 = ""
    city = ""
    state = ""
    zip = ""

# Address 인스턴스 생성
homeAddress = Address()

# Address 속성 값 지정
homeAddress.name = "이상정"
homeAddress.line1 = "블라블라블라 주소"
homeAddress.line2 = "건물호수"
homeAddress.city = "시"
homeAddress.state = "도"
homeAddress.zip = "우편번호"

# 또 다른 Address 인스턴스 생성
vacationHomeAddress = Address()

# Address 속성 값 지정
vacationHomeAddress.name = "Jhon Smith"
vacationHomeAddress.line1 = "1122 Main Street"
vacationHomeAddress.line2 = ""
vacationHomeAddress.city = "Panama City Beach"
vacationHomeAddress.state = "FL"
vacationHomeAddress.zip = "32407"

# 주소 출력
def printAddress(address):
    print(address.name)
    if (len(address.line1) > 0):
        print(address.line1)
    if (len(address.line2) > 0):
        print(address.line2)
    print(address.city + ", " + address.state + " " + address.zip)

printAddress(homeAddress)
print()
printAddress(vacationHomeAddress)
