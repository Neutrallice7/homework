File = open("66690-0.txt", encoding="utf8")
data = File.read()

def word_count(data):
    counts = dict()
    words = data.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print(word_count(data))