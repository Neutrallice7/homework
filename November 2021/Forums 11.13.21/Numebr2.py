file1 = open("bro.txt", "r")
splits = file1.read().split(" ")
file2 = open("notbro.txt", "w")
numbers = 1

while numbers < len(splits):
    splits[numbers] = str(numbers) + "." + splits[numbers] + " "
    file2.write(splits[numbers])
    numbers += 1

file1.close()
file2.close()

