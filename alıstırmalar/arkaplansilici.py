from rembg import remove
input_path = 'silmedeneme.jpg'
output_path = 'output.png'
with open(r"BURAYA DOSYA UZANTISI VEYA DOSYA İSMİ", "rb") as input_file:  #dosya yolunu tam olarak belirtin
    with open(output_path, "wb") as output_file:
        output_file.write(remove(input_file.read()))
