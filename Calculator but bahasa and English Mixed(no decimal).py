print('Calculator Inggris campur Indo')
print('='*20)
print(' 1. Jumlah\t [+]')
print(' 2. Kurang\t [-]')
print(' 3. Pembagian\t [/]')
print(' 4. Perkalian\t [+]')
print('='*20)
calculator = input('pilih operasi 1/2/3/4:')
print('='*20)
bilangan_1 = int(input('Enter first number:'))
bilangan_2 = int(input('Enter second Number:'))
print('='*20)

if calculator =='1':
    print('user choosed Jumlah')
elif calculator =='2':
    print('user choosed Kurang')
elif calculator =='3':
    print('user choosed Pembagian')
elif calculator =='4':
    print('user choosed Perkalian')

if calculator =='1':
    hasil= bilangan_1+bilangan_2
    print("Result:",(bilangan_1+bilangan_2))

elif calculator =='2':
    hasil = bilangan_1-bilangan_2
    print("Result:",(bilangan_1-bilangan_2))

elif calculator =='3':
    hasil = bilangan_1/bilangan_2
    print("Result:",(bilangan_1/bilangan_2))

elif calculator =='4':
    hasil = bilangan_1*bilangan_2
    print("Result:",(bilangan_1*bilangan_2))




