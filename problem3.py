#problem 3 : 600851475143 sayısının en büyük asal çarpanı nedir? (600851475143 asal değildir)

n = 600851475143    

list = []

i = 2
while i <= n:
    while n % i == 0:
        n = n / i
        for j in range(2,i):
            if i % j ==0:
                break
        else:
            list.append(i)

    i += 1

print(max(list))



                
            
