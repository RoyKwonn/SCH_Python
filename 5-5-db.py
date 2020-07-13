import sqlite3 # SQLite3 라이브러리 

def find_details(id2find):
    db = sqlite3.connect("surfersDB.sdb")    # 데이터베이스 연결 
    db.row_factory = sqlite3.Row            # 열 이름으로 참조
    cursor = db.cursor()
    cursor.execute("select * from surfers") # 테이블의 모든 행 읽음
    rows = cursor.fetchall()                # 읽은 행을 rows에 저장

    for row in rows:
        if row['id'] == id2find:
            s = {}
            s['id'] = str(row['id'])
            s['name'] = row['name']
            s['country'] = row['country']
            s['average'] = str(row['average'])
            s['board'] = row['board']
            s['age'] = str(row['age'])
            cursor.close()
            return(s)
    cursor.close()
    return({})

lookup_id = int(input("Enter the id of the surfer : "))
surfer = find_details(lookup_id)
if surfer:
    print("ID :             " + surfer['id'])
    print("Name :           " + surfer['name'])
    print("Country :        " + surfer['country'])
    print("Averate :        " + surfer['average'])
    print("Board type :     " + surfer['board'])
    print("Age :            " + surfer['age'])
        
