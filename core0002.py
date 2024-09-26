name = "adham"
lastname = "ibrohimiy"
name_lastname = f"{name} {lastname}"
print(name_lastname.upper()) #hamma harrflarni kattartirib beradi
print(name_lastname.lower()) #hammasini kichraytirib beradi
print(name_lastname.title()) #matndagi barcha sozlarni birinchi harflarni katta qilib beradi
print(name_lastname.capitalize()) #matndagi faqat birinchi sozni birinchi harfini kattartirib beradi

#strip() - matn boshi va oxiridagi boshliqni olib tashlaydi
#rstrip() - matn oxiridagi boshliqni olib tashlaydi
#lstrip() - matn boshidagi boshliqni olib tashlaydi
fruit = "   apple   "
print(fruit.strip())
print(fruit.rstrip())
print(fruit.lstrip())

#INPUT
word = input("Hi ! what is your name ")
print("Nice to meet you " + word)


