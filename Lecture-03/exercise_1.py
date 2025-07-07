Eng = float(input('Plase input your English score: '))
sci = float(input('Plase input your science score: '))
Compro = float(input('Plase input your Compro score: '))

average = (Eng+sci+Compro)/3
print(average)
if average >95:
    print('Congratulations')
else:
    print ('Get out!')


