fruits = ['aplle','pear','fig','peach']
costs = [23000,49999,30000,50000]
cars = []
print(f"first fruit: {fruits[0]}")
print(f"first fruit: {fruits[0].title()}")
print(f"first fruit: {fruits[0].upper()}")
print(f"first fruit: {fruits[0].lower()}")
print(f"first fruit: {fruits[0].capitalize()}")
print(f"Total cost: {costs[0] + costs[1]}")#agar indexni - bilan bersak masalan: cost[-1] list oxiridagi son chiqadi

#########################################################
#list elementlarini o'zgartirish


print(f"Before: {fruits}\n       {costs}\n       {cars}")
fruits[0] = 'apple  juice'
costs[2] += 2000
fruits.append("carrot")#listga ma'lumot qo'shish
cars.append("lacetti")
cars.append("lacetti")
cars.append("gentra")
cars.append("KIA K5")
cars.append("Tahoe")
cars.append("KIA K8")
cars.append("Chery")


#ROYXATNI ISTALGAN JOYIGA ELLEMENT QOSHISH


cars.insert(2,"Equinox")
print(f"After: {fruits}\n       {costs}\n       {cars}")


#INDEXGA MUROJAAT QILISH ORQALI LIST ELEMENTINI OCHIRISH


del costs[3]
fruits.remove('fig')

#########################################################
#LISTDAN ELEMENT SUG'IRIB OLISH.
# AGAR POP() DA QAVS ICHIGA SON YOZMASAK LIST OXIRIDAN ELEMENT OCHIRADI


find = cars.pop(3)
print("I bought " + find + " 3 month ago")
print(f"After2: {fruits}\n       {costs}\n       {cars}")
#ROYXATNI TARTIBLASH SORT agar element togri tartiblanishini istasangiz ularni bosh harfini bir xil katta yoki kichik qilib olish kk
#yo'qsa katta harflar boshiga chiqib ketadi
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
# SORTED(list,reverse=true) va SORT() NI FARQI 1- HOLATNI PRINT() BILAN QOLLASA HAM BOLADI 2-CHISINI ESA PRINT() ICHIGA YOZIB BOMAYDI
print(sorted(fruits,reverse=True))
#RANGE() FUNKSIYASINI ISHLATISH
number = list(range(0,10))
print(number)
print(len(number))
juft_numbers = list(range(0,20,2))
toq_sonlar = list(range(1,20,2))
print(juft_numbers)
print(toq_sonlar)
#min max sum
minimum = min(juft_numbers)
maximum = max(toq_sonlar)
sums = sum(number)
print(minimum)
print(maximum)
print(sums)

#ROYXATNI KESISH. pythonda kesish 2-korsatilgan indexdan bitta oldin toxtaydi
my_cars = cars[0:4]#0 dan boshlab 4  ta elementni ajratib my_list listiga qoshadi
my_cars2 = cars[2:5]# 2 3 4 chi elementlarni chop etadi
my_cars3 = cars[:4]#royxat boshidan 4ta element ajratish
my_cars4 = cars[2:]#2-elementdan royxat oxirigacha bolgan elementni ajratish
print(my_cars)
#ROYXATNI NUSXALASH
cars2 = cars
cars2.append('bmw')
cars2.append('Bugatti chiron')
print('cars2: ',cars2)
print("cars: ", cars)# ELEEMENT FAQAT CARS2 GA QOSHILDI AMMO U CARS NING NUSXASI BOLGANI UCHUN ELEMENT CARS LISTGA HAM QOSHILDI
#ROYXATNI KOCHIRIB OLISH
cars3 = cars[:]# [:] BU ROYXATNI TOLIQ KOCHIRADI KOCHIRGANDA MALUMMOT FAQAT BIRIGA QOSHILADI
cars3.append("malibu")
print(cars3)
print(cars)

"""
Tuples Royxatlar - o'zgarmas royxatlar ularga ma'lumot dastur boshida () -> sshu kabi qavsda beriladi va
unni ichidagi malumotlar endi ozgartirib bolmas holatga keeladi.
"""
tuple1 = (1,2,3,4,5)
print(tuple1)
print(type(tuple1))
#########################################################
"""
Agar tuple ga ozgartirish kerak bolsa avval uni listga ogirib ozgartirish kiritib
olib songra uni yana tuple typega qaytarib qoyish kerak
"""
tuple1 = list(tuple1)
print(type(tuple1))
tuple1.append(5)
tuple1 = tuple(tuple1)

print(tuple1)
#########################################################
#FOR SIKLI royxatlar bilan
guests = ['adam','john','maria','lisa']
for guest in guests:
    print(guest.title())

##################################################################################################################
numbers = list(range(1,11))
for number in numbers:
    print(f"{number} ning kvadrati-> {number**2}")

kv_numbers = []
for number in numbers:
    kv_numbers.append(number**2)

print(f"kvadrat list: {kv_numbers}")


names = []
for name in range(5):
    names.append(input(f"{name + 1}-ismni kiriting"))
print(names)