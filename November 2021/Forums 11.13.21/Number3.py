initial = open("66690-0.txt",encoding="utf-8")
file = initial.read
count1=0
count2=0
for line in initial:
    count1+=1
    words=line.rstrip().split()
for word in words:
    count2+=1
average=count1/count2
print('Average words per line: ',average)