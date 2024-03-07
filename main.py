n=int(input())
sum=0
for Par in range(1,n+1):
    if Par%2==0:
        sum+=Par
print("La suma de todos los numeros que son primos: ",sum)