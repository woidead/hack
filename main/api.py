import requests

sneakers_API = 'https://abdullaev012.pythonanywhere.com/'
res = requests.get(sneakers_API)
data = res.json()
land = len(data)
i = 0
ii = []
while i != land:
    i = i + 1
    ii.append(i)
ii.insert(0, 0)
ii.pop()
id = []
sneakers_name = []
description = []
image = []
price = []
for y in ii:
    id.append(data[y]['id'])
    sneakers_name.append(data[y]['sneakers_name'])
    description.append(data[y]['description'])
    image.append(data[y]['image'])
    price.append(data[y]['price'])
zipped_values = zip(id, sneakers_name, description, image, price)

lists = list(zipped_values)