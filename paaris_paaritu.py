# Teeme Pythoni programmi, mis tuvastab paaris ja paarituid arve
# Number on paaris, kui jagades kahega on ta jääk 0, nt 8/2 = 4.0

number = int(input("Sisesta number: "))
if (number % 2) == 0:
   print("{} on paarisarv".format(number))
else:
   print("{} ei ole paarisarv".format(number))