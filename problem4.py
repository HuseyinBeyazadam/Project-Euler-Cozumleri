# Problem 4 : iki adet 3 basamaklı sayının çarpımıyla elde edilebilecek en büyük palindrom sayıyı bul. (Palindrom sayı, tersten okunduğunda da aynı olan sayıdır.)

# Adım 1 : 3 basamaklı tüm sayıları çarpalım

list = []

for i in range(100 , 1000):
    for j in range(100 , 1000):
        sayi = i * j
        ters = str(sayi)[::-1]
        if str(sayi) == ters :
            list.append(sayi)

print(max(list))