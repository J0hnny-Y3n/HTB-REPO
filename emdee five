

import requests 
import re
import hashlib



# basic display the web site contents
url = "http://docker.hackthebox.eu:31977/"
s = requests.session()
r = s.get(url)
print(r.text)


# use regex to get 20-char MD5 string that needs to be encoded
MD5_string = re.findall(r'(\w{20})', r.text)
#print("Here's the list", MD5_string)


# convert from list to string
newMD5 = str(MD5_string).strip('[]')
#print("Here's the string",newMD5)


# encode (encrypt) the new MD5 string
result = hashlib.md5(newMD5.encode()).hexdigest()
#print("Here's the hash", result)


# how to do the lines above separetely
# encoded = newMD5.encode()
# h = hashlib.md5(encoded)
# print(h.hexdigest())


cookie = r.headers['Set-Cookie']
cookie = cookie.replace("; path=/","")
cookie = cookie.replace("PHPSESSID=","")



payload = {'hash':result}
finalPost = s.post(url,payload, cookie)
print(finalPost.text)
