from downloadImages import download, listFile
import functools

url = [
    "https://i.pinimg.com/564x/0e/d6/23/0ed623806cf3b9d805a8cb1e4c822daf.jpg",
    "https://i.pinimg.com/564x/6b/2d/59/6b2d5980bce5a2d7024e95afabf21988.jpg",
    "https://i.pinimg.com/564x/99/71/c1/9971c1d4883cd1429851ced56cb6db5b.jpg",
    "https://i.pinimg.com/564x/b7/5a/95/b75a95e35fe629cb60e91b08312e506c.jpg",
    "https://i.pinimg.com/564x/8c/36/50/8c3650e5343c3289b353125155640fcd.jpg",
    "https://i.pinimg.com/564x/41/d9/ae/41d9aeace30eca2a00dbde5ad3321f26.jpg",
    "https://i.pinimg.com/564x/63/dd/83/63dd8347e43604e06a05f37fdc420427.jpg",
    "https://i.pinimg.com/564x/9d/ad/1e/9dad1e895e3998f113be295c8dbbba17.jpg",
    "https://i.pinimg.com/564x/df/ae/2a/dfae2a7cba82da6d02fe78ac4f24fae6.jpg",
    "https://i.pinimg.com/564x/a9/61/34/a96134950b4591b8a99dab63a75e3849.jpg"
]

allStatus = []

for i in range (10):
    r = download.delay(url[i], 'property'+str(i)+'.png')
    allStatus.append(r)

currentAllStatus = [x.status != "PENDING" for x in allStatus]

# flag = True
# while(flag):
#     flag = functools.reduce(lambda a,b: True if a == True or b == True else False, currentAllStatus)