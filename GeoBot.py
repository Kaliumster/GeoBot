from urllib.request import urlopen
from urllib.parse import quote
import json

filein = open("list.txt", "r")
contents = filein.read().split("\n")
fileout = open('coordinates.txt','w')
for address in contents:
    url = "https://maps.googleapis.com/maps/api/geocode/json?address="+quote(address)+"&key=INSERT_YOUR_GOOGLE_API_KEY_HERE"
    f = urlopen(url).read()
    f = json.loads(f.decode('utf-8'))
    print("Searching "+address+"...")
    if len(f['results']) == 0:
        out=address+"\t NOT FOUND"
    else:
        answer = f['results'][0]
        lat=answer.get('geometry').get('location').get('lat')
        long=answer.get('geometry').get('location').get('lng')
        out=address+"\t \t"+str(lat)+"\t"+str(long)    
    print(out)
    fileout.write(out+"\n")
fileout.close()
filein.close()
