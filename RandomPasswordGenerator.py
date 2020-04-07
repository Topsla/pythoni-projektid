import random

pikkus = int(input('Palun sisesta siia soovitud parooli pikkus: '))

def genereeri(pikkus):
    parool = str()
    märgid = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&/()*+,-./:;?@[]^_`{|}~'
    for i in range (pikkus):
        parool = parool + random.choice(märgid)
    print('Sinu parool on: ' + parool + '. See koosneb ' + str(pikkus) + ' märgist!')
    return

genereeri(pikkus)




























