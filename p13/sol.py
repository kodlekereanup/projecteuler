f = open('input.txt', 'r').readlines()

sume = 0
for line in f:
    sume += int(line)

print(sume[:10])
