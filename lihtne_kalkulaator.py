#Programmeerime lihtsa kalkulaatori

#Liitmine
def liida (x, y):
   return x + y

#Lahutamine
def lahuta (x, y):
   return x - y

#Korrutamine
def korruta (x, y):
   return x * y

#Jagamine
def jaga (x, y):
   return x / y

print("Vali tehe")
print("1. Liitmine")
print("2.Lahutamine")
print("3. Korrutamine")
print("4. Jagamine")

#Kasutaja sisend
valik = input("Vali tehe (1/2/3/4): ")

number1 = float(input("Sisesta esimene number: "))
number2 = float(input("Sisesta teine number: "))

if valik == "1":
   print(number1, "+" , number2, "=", liida(number1,number2))
elif valik == "2":
   print(number1, "-" , number2, "=", lahuta(number1,number2))
elif valik == "3":
   print(number1, "*" , number2, "=", korruta(number1,number2))
elif valik == "4":
   print(number1, "/" , number2, "=", jaga(number1,number2))
else:
   print("Vale sisend!")