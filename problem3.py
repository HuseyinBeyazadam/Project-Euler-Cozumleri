#problem 3 : 600851475143 sayısının en büyük asal çarpanı nedir? (600851475143 asal değildir)

n = 600851475143    

list = [] 

i = 2
while i <= n: #Adım 1 : n sayısını çarpanlarına ayırmalıyız. 
    while n % i == 0:
        n = n / i #Adım 2 : sayı çok büyük bu yüzden sürekli çarpanlarına bölerek sayıyı küçültüp deneme sayımızı azaltmalıyız.
        for j in range(2,i): #Adım 3 : çarpanların asallığını kontrol edip listeye ekleyelim
            if i % j ==0:
                break
        else:
            list.append(i)

    i += 1

print(max(list)) #Adım 4 : listeden en büyük asal çarpanı ekrana yazdıralım.



                
            
