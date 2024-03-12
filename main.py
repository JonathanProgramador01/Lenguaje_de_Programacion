# Size=3
# Base=[]


# for i in range(Size):
#     num=int(input())
#     Base.append(num)

# Max=Base[0]

# for i in range(Size):
#     if Max<Size:
#         Max=Size

# print(f"Numero max:  {Max}")
def factorial (n):
    if n ==1:
        return 1
    return n*factorial(n-1)


n=int(input("Calculadora del Factorial: "))
print(factorial(n))



