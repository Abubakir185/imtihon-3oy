# Imtihon qoidalari, aldamang, atrofga qaramang!
# Savollarga javob yozing va namuna kodini taqdim eting.



# 1-savol: Pythonda funksiya nima?

#Javob:
# bizni ishimizni osonlashtirish uchun ishlatiladigan ish qurollari ular python tomonidan berilgan boladi yoki ozimiz yaratishimiz mumkin
# Kod namunasi:

# sum(), max(), min(), print()  
# def name(argument):

    # return



# 2-savol: Pythonda funktsiyani qanday e'lon qilish mumkin?

#Javob:
# funksiya ismi oxiriga qovus qoyib
# Kod namunasi:

# name()



# 3-savol: Funktsiyaga argumentlarni qanday o'tkazish mumkin?

#Javob:
# Kod namunasi:
# def time_two(num)
    # num_2 = num * 2
    # return num





# 4-savol: Standart (default) argumentlar nima va ularni funktsiyada qanday ishlatish kerak?

#Javob:
# agar foydalanuvchi argumentga qiymat bermasa tenglab qoyilgan qiymatni oladi
# Kod namunasi:
# def name(name = "", age = 0)

#   return



# 5-savol: Funksiya ichidagi return va print() ko'rsatmalari o'rtasidagi farq nima?

#Javob:
# return bu qiymatni qaytaradi print() uni ekranga chiqaradi
# Kod namunasi:



#6-savol: Python-da class nima va u nima uchun ishlatiladi?

#Javob:
# Kod namunasi:



# 7-savol: Python-da classni qanday e'lon qilish kerak?

#Javob:
# Kod namunasi:
# class Inson:
#   def __init__(self, name, age):
#       self.name = name
#       self.age = age

# abubakir = Inson("Abubakir", 14)



# 8-savol: Class (ob'ekt) misolini qanday yaratish mumkin?

#Javob:
# Kod namunasi:
# class Inson:
#   def __init__(self, name, age):
#       self.name = name
#       self.age = age

# abubakir = Inson("Abubakir", 14)

# 9-savol: Python-da o'rnatilgan(dunder) class metodlari qanday?

#Javob:
# __init__ funksiyasi class yaratilganda har doim birinchi bolib yoziladi, __str__ objectni string qilib qaytaradi
# Kod namunasi:
# class Name:
#     def __init__(self) -> None:
#         pass
# def __str__()



# 10-savol: Class konstruktorini qanday yaratish kerak va u nima uchun kerak?

#Javob:
# Kod namunasi:
# class Inson:
#   def __init__(self, name, age):




#11-chi mini loyiha:

class Product:
    def __init__(self, name, price, spare, cotegory):
        self.name = name
        self.price = price
        self.spare = spare
        self.cotegory = cotegory

    def add_product(self, name, price, amount):
        if self.name == name:
            self.spare += amount
            print(f"{name} mavjud. Miqdor yangilandi. Yangi miqdor: {self.spare}")
        else:
            self.name = name
            self.price = price
            self.spare = amount
            print(f"Yangi tovar qo'shildi: {name}, Narxi: {price}, Miqdor: {amount}")

    def take_product(self, amount):
        if amount <= self.spare:
            self.spare -= amount
        else:
            print(f"Bu maxsulotdan {amount} mavjud!")



class Book(Product):
    def __init__(self, name, price, spare, cotegory, author, ganre, pages):
        super().__init__(name, price, spare, cotegory)
        self.author = author
        self.ganre = ganre
        self.pages = pages


class Clothes(Product):
    def __init__(self, name, price, spare, cotegory, size):
        super().__init__(name, price, spare, cotegory)
        self.size = size


class Electronics(Product):
    def __init__(self, name, price, spare, cotegory, brand):
        super().__init__(name, price, spare, cotegory)
        self.brand = brand


class Cart:
    def __init__(self):
        self.products = []
        self.total_price = 0

    def add_product(self, product, quantity):
        self.products.append((product, quantity))
        self.total_price += product.price * quantity

    def show_total_price(self):
        print(f"Total price: {self.total_price}")

    def order(self):
        for product, quantity in self.products:
            if product.take_product(quantity):
                self.total_price -= product.price * quantity
        print(f"Order placed successfully. Total price: {self.total_price}")
        self.products = []  
        self.total_price = 0 


book = Book("Python Programming", 30, 10, "Books", "John Doe", "Programming", 200)
clothes = Clothes("T-Shirt", 15, 50, "Clothes", "L")
electronics = Electronics("Laptop", 1000, 5, "Electronics", "Brand X")

cart = Cart()
cart.add_product(book, 2)
cart.add_product(clothes, 3)
cart.show_total_price()

cart.order()

