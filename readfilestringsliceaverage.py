# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    stnum = line.find(' ')
    ssnum = line.find('\n')
    number = float(line[stnum+1:ssnum])
    total = total + number
average = (total/count)
print "Average spam confidence:", average
