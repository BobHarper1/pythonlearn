name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts=dict()
for line in handle:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    time = words[5]
    hour = time[0:2]
    if hour not in counts:
        counts[hour] = 1
    else:
        counts[hour]+= 1

lst = list()
for key, val in counts.items():
    lst.append((key, val))
lst.sort()
for key, val in lst:
    print key, val
