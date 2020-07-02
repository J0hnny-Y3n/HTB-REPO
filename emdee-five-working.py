# stolen from https://sarthaksaini.com/2019/June/web-app/emdee-five-for-life.html

import requests
import hashlib
import re

url="http://docker.hackthebox.eu:30383/"

r=requests.session()
out=r.get(url)
print(out.text)

out=re.search("<h3 align='center'>+.*?</h3>",out.text)
print(out)
out=re.search("'>.*<",out[0])
print(out)
out=re.search("[^|'|>|<]...................",out[0])
print(out)


out=hashlib.md5(out[0].encode('utf-8')).hexdigest()
print(out)


print("sending md5 :-{}".format(out))

data={'hash': out}
out = r.post(url = url, data = data)

print(out.text)
