name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
d = dict()
for line in handle:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    sender = words[1]
    if words[1] not in d:
        d[words[1]] = 1
    else:
        d[words[1]] += 1
largest = None
for value in d:
    if largest is None or d[value] > largest :
        largest = d[value]
        print value, d[value]
