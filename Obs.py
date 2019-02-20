# Obs sistemi
sayac = int(input("lutfen öğrenci sayısını giriniz."))
i = 0
while (sayac>i):
    sayac -= 1
    mat(vize,final)
    genelisletme(vize,final)
    edebiyat(vize,final)
    finansal(vize,final)
    proglamlama(vize,final)
    inglizce(vize,final)
    inkilap(vize,final)

def mat(vize,final):
   print()
vize = int(input("Matematik Vize notunuzu girinz lutfen:"))
final = int(input("Matematik Final notunzu giriniz lutfen:"))
ortalama = vize*30/100 + final*70/100
if ortalama >=85:
    print("Matematik Harf Notunuz:AA")
elif ortalama>=70 and ortalama<85:
    print("Matematik Harf Notunuz:BA")
elif ortalama>=60 and ortalama<70:
    print("Matematik Harf Notunuz:BB")
elif ortalama>=50 and ortalama<60:
    print("Matematik Harf Notunuz:CC")
else:
    print("Matematik dersinden maalesef Gecemediniz.")


# -------------------------------------------------------------

def inkilap(vize,final):
   print()
vize = int(input("İnkilap Vize notunuzu girinz lutfen:"))
final = int(input("İnkilap Final notunzu giriniz lutfen:"))
ortalama = vize*30/100 + final*70/100
if ortalama >=85:
    print("İnkilap Harf Notunuz:AA")

elif ortalama>=70 and ortalama<85:
    print("İnkilap Harf Notunuz:BA")
elif ortalama>=60 and ortalama<70:
    print("İnkilap Harf Notunuz:BB")
elif ortalama>=50 and ortalama<60:
    print("İnkilap Harf Notunuz:CC")
else:
    print("İnkilap dersinden  maalesef Gecemediniz.")




# ---------------------------------------------------------------
def inglizce(vize,final):
    print()
vize = int(input("İnglizce Vize notunuzu girinz lutfen:"))
final = int(input("İnglizce Final notunzu giriniz lutfen:"))
ortalama = vize*30/100 + final*70/100
if ortalama >=85:
    print("İnglizce Harf Notunuz:AA")
elif ortalama>=70 and ortalama<85:
    print("İnglizce Harf Notunuz:BA")
elif ortalama>=60 and ortalama<70:
    print("İnglizce Harf Notunuz:BB")

elif ortalama>=50 and ortalama<60:
    print("İnglizce Harf Notunuz:CC")
else:
    print("İnglizce dersinden maalesef Gecemediniz.")


# ---------------------------------------------------------------

def proglamlama(vize,final):
    print()
vize = int(input("Proglamlama Vize notunuzu girinz lutfen:"))
final = int(input("Proglamlama Final notunzu giriniz lutfen:"))
ortalama = vize*30/100 + final*70/100
if ortalama >=85:
    print("Proglamlama Harf Notunuz:AA")
elif ortalama>=70 and ortalama<85:
    print("Proglamlama Harf Notunuz:BA")
elif ortalama>=60 and ortalama<70:
    print("Proglamlama Harf Notunuz:BB")
elif ortalama>=50 and ortalama<60:
    print("Proglamlama Harf Notunuz:CC")
else:
    print("Proglamlama dersinden maalesef Gecemediniz.")



# ------------------------------------------------------------------
def finansal(vize,final):
    print()
vize = int(input("Finansal Vize notunuzu girinz lutfen:"))
final = int(input("Finansal Final notunzu giriniz lutfen:"))
ortalama = vize*30/100 + final*70/100
if ortalama >=85:
    print("Finansal Harf Notunuz:AA")
elif ortalama>=70 and ortalama<85:
    print("Finansal Harf Notunuz:BA")
elif ortalama>=60 and ortalama<70:
    print("Finansal Harf Notunuz:BB")
elif ortalama>=50 and ortalama<60:
    print("Finansal Harf Notunuz:CC")
else:
    print("Finansal dersinden maalesef Gecemediniz.")




# ----------------------------------------------------------
def edebiyat(vize,final):
   print()
vize = int(input("Edebiyat Vize notunuzu girinz lutfen:"))
final = int(input("Edebiyat Final notunzu giriniz lutfen:"))
ortalama = vize*30/100 + final*70/100
if ortalama >=85:
    print("Edebiyat Harf Notunuz:AA")
elif ortalama>=70 and ortalama<85:
    print("Edebiyat Harf Notunuz:BA")
elif ortalama>=60 and ortalama<70:
    print("Edebiyat Harf Notunuz:BB")
elif ortalama>=50 and ortalama<60:
    print("Edebiyat Harf Notunuz:CC")
else:
    print("Edebiyat dersinden maalesef Gecemediniz.")



# -----------------------------------------------------------
def genelisletme(vize,final):
   print()
vize = int(input("Genelisletme Vize notunuzu girinz lutfen:"))
final = int(input("Genelisletme Final notunzu giriniz lutfen:"))
ortalama = vize*30/100 + final*70/100
if ortalama >=85:
    print("Genelisletme Harf Notunuz:AA")
elif ortalama>=70 and ortalama<85:
    print("Genelisletme Harf Notunuz:BA")
elif ortalama>=60 and ortalama<70:
    print("Genelisletme Harf Notunuz:BB")
elif ortalama>=50 and ortalama<60:
    print("Genelisletme Harf Notunuz:CC")
else:
    print("Genelisletme dersinden maalesef Gecemediniz.")
# ---------------------------------------------------
