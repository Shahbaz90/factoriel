__author__ = 'Shahbaz_Akhtar'
number= int(input("Enter a number : "))
factorial=1
for counter in range(number,1,-1):
    factorial=factorial * counter
print(factorial)
