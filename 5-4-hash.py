def find_details(id2find):
    surfers_f = open("surfing_data.csv");
    for eachline in surfers_f:
        s = {}
        (s['id'], s['name'], s['country'], s['average'], s['board'], s['age']) = eachline.split(";")
        if id2find == int(s['id']):
            surfers_f.close()
            print(s)
            print('--------------')
            return(s)
    surfers_f.close()
    return({})

lookup_id = 0

while lookup_id != -1:
    lookup_id = int(input("Enter the id of the surfer : "))
    surfer = find_details(lookup_id)
    if surfer:
        print("ID :           " + surfer['id'])
        print("Name :         " + surfer['name'])
        print("Country :      " + surfer['country'])
        print("Average :      " + surfer['average'])
        print("Board type :   " + surfer['board'])
        print("Age :          " + surfer['age'])
    elif lookup_id == -1:
        break
    else:
        print("선수 없음")
