import os

a = os.walk('/home/luv/notes/Notes/DailyWork/')
a.next()
words = {}
while True:
    try:
        info = a.next()
    except StopIteration:
        break
    path = os.path.join(info[0], "words")
    with open(path) as f:
        lines = f.readlines()
        for line in lines:
            if line[0] == " " or line[0] == "\t"\
                    or line == "" or line[0] == "\n":
                continue
            d = line.split(":", 1)
            try:
                words[d[0]] = d[1]
            except IndexError:
                pass
for key in words:
    print key+":  "+words[key]

print len(words)
