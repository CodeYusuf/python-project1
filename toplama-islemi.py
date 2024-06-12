# ****************** Yusuf Göktuğ Aydemir ****************** #
  # ***************** Python Örnekleri ********************* #
sayi1 = int(input("1.sayıyı giriniz :"))
sayi2 = int(input("2.sayıyı giriniz :"))
islem = input("İşlem seçiniz :")
toplama = sayi1 + sayi2
cikarma = sayi1 - sayi2
carpma  = sayi1 * sayi2
bolme   = sayi1 / sayi2

if(islem =="+"):
    print(toplama)

elif(islem == "-"):
    print(cikarma)

elif(islem == "*"):
    print(carpma)

else:
    print(bolme)