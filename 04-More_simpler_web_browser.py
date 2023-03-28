import urllib.request

fhand = urllib.request.urlopen("http://localhost:9000/remeo.html")
for line in fhand:
    print(line.decode().strip())

