#Get the user's name, are, and income.
name = input('What is your name?: ')
aeg = int(input('What is your age?: '))
income = float(input('What is your income?: '))

#Display the data.
print('Here is the data you entered:')
print('Name:', name)
print('Age:', aeg)
print('Income:', format(income, '12,.2f'))
