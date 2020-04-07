import random

nimi = input("Tere! Mis on sinu nimi? ")
print("Tore kohtuda, " + nimi + "! Ma mõtlen ühele numbrile 1-20 vahel. Sul on viis katset seda arvata!")

õigeNumber = random.randint(1,20)

for katseid in range(1,6):
    sinuNumber = int(input("Arva ära: "))

    if sinuNumber < õigeNumber:
        print("Mõtle suurema numbri peale.")
    elif sinuNumber > õigeNumber:
        print("Mõtle väiksema numbri peale.")
    else:
        break #Kui ei vasta kahele ülemisele tingimusele, siis sinuNumber on õige!

if sinuNumber == õigeNumber:
    print("Tubli töö, " + nimi + "! Sa arvasid õige numbri ära " + str(katseid) + " katsega!")
else:
    print("Sa ei arvanud ära õiget numbrit. Õige number oli " + str(õigeNumber) + ".")
