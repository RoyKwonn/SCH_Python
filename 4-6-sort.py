scores = []

f = open("results.txt")

for line in f:
    (name, score) = line.split()
    scores.append(float(score))
f.close()

scores.sort()
scores.reverse()

print(scores[0])
print(scores[1])
print(scores[2])
