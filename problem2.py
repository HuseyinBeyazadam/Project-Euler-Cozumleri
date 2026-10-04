#Problem 2 : fibonacci sayılarının 4 milyondan küçük olanlarını bulup bu sayılardan çift olanların toplamını bulmamızı istiyor.

#Adım 1: Fibonacci sayıları bulmalıyız fibonacci sayıların kendisinden iki öncek sayının toplamı şeklinde ilerler Örn: 0, 1, 1, 2, 3, 5, 8, 13, 21 şeklinde ilerler.
#
number1 = 0
number2 = 1
sum = 0

fibonacci = 0

while fibonacci < 4000000:
    fibonacci = number1 + number2
    number1 = number2
    number2 = fibonacci
    if fibonacci % 2 == 0: #Adım2 bulduğumuz fibonacci sayılarını çif olanları bulmamız ve bir yerde toplamamız gerekiyor.
        sum += fibonacci

print(sum) #Adım 3: Son olarak toplamı ekrana yazdırmamız gerekiyor.