f = open("results.txt")

score = 0

for line in f:
    (name, sc) = line.split()
    if float(sc) > score:
        score = float(sc)

f.close()

print("최고점수 : ", score)
