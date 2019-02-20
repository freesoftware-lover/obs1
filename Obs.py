# Obs sistemi
#!/bin/python3

def ortalama(vize, final):
    ort = vize*30/100 + final*70/100

    if ort >=85:
        print("Harf Notunuz:AA")
    elif ort>=70 and ort<85:
        print("Harf Notunuz:BA")
    elif ort>=60 and ort<70:
        print("Harf Notunuz:BB")
    elif ort>=50 and ort<60:
        print("Harf Notunuz:CC")
    else:
        print("Dersi maalesef gecemediniz.")

def mat():
    vize = int(input("Matematik Vize notunuzu giriniz lütfen: "))
    final = int(input("Matematik Final notunzu giriniz lütfen: "))
    return ortalama(vize, final)


def inkilap():
   vize = int(input("İnkılap Vize notunuzu giriniz lütfen: "))
   final = int(input("inkılap Final notunzu giriniz lütfen: "))
   return ortalama(vize, final)

def ingilizce():
    vize = int(input("inglizce Vize notunuzu giriniz lütfen: "))
    final = int(input("inglizce Final notunzu giriniz lütfen: "))
    return ortalama(vize, final)

def programlama():
    vize = int(input("Proglamlama Vize notunuzu giriniz lütfen: "))
    final = int(input("Programlama Final notunzu giriniz lütfen: "))
    return ortalama(vize, final)

def finansal():
    vize = int(input("Finansal Vize notunuzu giriniz lütfen: "))
    final = int(input("Finansal Final notunzu giriniz lütfen: "))
    return ortalama(vize, final)

def edebiyat():
   vize = int(input("Edebiyat Vize notunuzu giriniz lütfen: "))
   final = int(input("Edebiyat Final notunzu giriniz lütfen: "))
   return ortalama(vize, final)

def genel_isletme():
   vize = int(input("Genel İşletme Vize notunuzu giriniz lütfen: "))
   final = int(input("Genel İşletme Final notunzu giriniz lütfen: "))
   return ortalama(vize, final)

while True:
    giris = int(input("Lütfen öğrenci sayısını giriniz (Çıkış için -1): "))
    if giris == -1:
        print("Program sonlanıyor.")
        break
    for i in range(1, giris + 1):
        mat()
        inkilap()
        ingilizce()
        programlama()
        finansal()
        edebiyat()
        genel_isletme()
