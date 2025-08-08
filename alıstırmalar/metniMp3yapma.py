from gtts import gTTS
import os
from tkinter import Tk, filedialog

secim = int(input("metni sesli okumak için 1, belgeyi sesli okumak için 2'ye basın: "))
if secim == 1:
    metin = input("Sesli okunacak Türkçe metni yazın: ")
    tts = gTTS(text=metin, lang='tr')
    tts.save("ses.mp3")
    # os.system("start ses.mp3")       program bittikten hemen sonra mp3 dosyasını açar
elif secim == 2:
    root = Tk()
    root.withdraw()
    root.lift()
    root.attributes('-topmost', True)
    dosya_adi = filedialog.askopenfilename(
        title="Sesli okunacak belgeyi seçin",
        filetypes=[("Metin Dosyaları", "*.txt"), ("Tüm Dosyalar", "*.*")]
    )
    root.destroy()
    if dosya_adi:
        try:
            with open(dosya_adi, 'r', encoding='utf-8') as dosya:
                metin = dosya.read()
            tts = gTTS(text=metin, lang='tr')
            tts.save("ses.mp3")
            # os.system("start ses.mp3")       program bittikten hemen sonra mp3 dosyasını açar
        except FileNotFoundError:
            print(f"{dosya_adi} bulunamadı.")
    else:
        print("Herhangi bir dosya seçilmedi.")
