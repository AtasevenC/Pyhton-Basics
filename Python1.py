#SAYILAR VE STRINGLERE GIRIS

print("Hello AI ERA")

9*2


"Hello AI ERA"

'Hello AI ERA'

9 #int

9.2 #float

9 + 9 #matematiksel islem

#STRINGLER

type(123)

type("Ali")

type("123")


#STRING METODLARI

len("Merhabalar!")

len("MVK")

#atama islemi ve degisken olusturma

hi = "Hello AI ERA"

#del hi

len(hi)


#upper() & lower()

UP_HI = hi.upper()

UP_HI

hi

UP_HI.lower()

hi.isupper()
UP_HI.isupper()
UP_HI.islower()


#replace()

hi = hi.replace("l","p")

hi

dir(hi)


a = "123"

a.isdigit()


hi.title()



txt = "Welcome to My world"

x = txt.title()

print(x)

x.capitalize()


# SUBSTRINGLER

hi = "Hello AI ERA"

hi[0]

hi[7]

hi[6:8] #slicing

hi[9:12]

#DEGISKENLER

a = 9
a

b = 10

a * b

#KULLANICIDAN BILGI ALMA & TIP DONUSUMLERI

number = input()
number*3

type(number)


type(int(number))

int(number)*3

num1 = int(input())
num2 = int(input())

num1*num2

def topla():
    
    print("Toplama yapmak için birinci sayıyı giriniz:")
    
    num1 = int(input())
    
    print("Toplama yapmak için ikinci sayıyı giriniz:")
    
    num2 = int(input())
    
    print("İşlem sonucunuz:")
    
    print(num1 + num2)
    
    
topla()


# VERI YAPILARI

## Listeler

notes = [1, 2, 3, 4]

type(notes)

notes[0:2]

names = ["Python", "R","SPSS"]

notNam = [1,2,3, "R","SPSS"]


notNam[3]


len(notes)

all_list = [names, notes]

all_list[0]

all_list[1]


# Liste Eleman İşlemleri


names = ["Ali","Veli","berkcan", "ayse"]


names[1] = "velinin_babasi"

names[3] = "ayse_new"


# Liste Metodları

"abc".upper()

names

#listeye eleman eklemek icin kullanılır
names.append("Mehmet")


#remove
names.remove("Mehmet")

#insert

names.insert(0, "Mehmet")

names = ["Ali","Veli","berkcan", "ayse"]

names.insert(0, "Mehmet")

names


#pop

names.pop(0)
names

dir(names)
names.insert(0, "ali")


liste_yedek = names.copy()

dir(list)


names.index("ayse")


# TUPLE

t = ("ali","veli",1,2)
t
type(t)
len(t)
t[0:3]
t[2] = 9

names = ["Ali","Veli","berkcan", "ayse"]
names[0] = "FILIZ"



# Dictionary (Sözlükler)

sozluk = {"REG": "Regresyon Modeli",
          "LOG": "Logistic Regression",
          "CART" : "Classification and Reg"}



sozluk

len(sozluk)

sozluk["REG"]


sozluk = {"REG" : 10,
          "LOJ" : 20,
          "CART" : 30}

sozluk["REG"]

sozluk = {"REG" : ["RMSE", 10],
          "LOJ" : ["MSE", 20],
          "CART" : ["SSE", 30]}


sozluk["REG"]




sozluk = {"REG": "Regresyon Modeli",
          "LOG": "Logistic Regression",
          "CART" : "Classification and Reg"}



sozluk["GBM"] = "Gradient Boosting Mac"


sozluk


#Veri Yapıları Özet Tablosu


