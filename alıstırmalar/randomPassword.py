import random
import string 
import pyperclip

secim=int(input("1 düz şifre oluştur,2- özel karakterli şifre oluştur: "))

match secim: 
    case 1:
        lenth = int(input("Lütfen şifrenin uzunluğunu giriniz: "))
        password = ''.join(random.choices(string.ascii_letters + string.digits , k=lenth))
        print("Oluşturulan şifre: ", password)
    case 2:
        lenth = int(input("Lütfen şifrenin uzunluğunu giriniz: "))
        password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=lenth))
        print("Oluşturulan şifre: ", password)

print("Şifre panoya kopyalandı.",pyperclip.copy(password))#otomatik ctrl+c ile panoya kopyalar